import os
import requests
from dotenv import load_dotenv
from langchain.llms.base import LLM
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.docstore.document import Document
from typing import Optional, List

# Load environment variables
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL = os.getenv("HF_MODEL")

# Custom Hugging Face API LLM Wrapper
class HuggingFaceLLM(LLM):
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {"Authorization": f"Bearer {HF_API_KEY}"}
        payload = {"inputs": prompt}
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{HF_MODEL}",
            headers=headers,
            json=payload
        )
        # data = response.json()
        # if isinstance(data, list) and len(data) > 0:
        #     return data[0].get("generated_text", "")
        # elif isinstance(data, dict) and "error" in data:
        #     return f"[Error] {data['error']}"
        # return str(data)
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            return f"[Error] Invalid JSON response from Hugging Face: {response.text}"

        if isinstance(data, list) and len(data) > 0:
            return data[0].get("generated_text", "")
        elif isinstance(data, dict) and "error" in data:
            return f"[Error] {data['error']}"
        return str(data)

    @property
    def _identifying_params(self) -> dict:
        return {"model": HF_MODEL}

    @property
    def _llm_type(self) -> str:
        return "huggingface-inference"

# Setup embeddings (using Hugging Face sentence transformers)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Setup Chroma persistent vector DB
PERSIST_DIR = "chroma_db"
vectorstore = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)

# Conversation memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Conversational retrieval chain
llm = HuggingFaceLLM()
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

def chat_with_bot(user_input: str) -> str:
    """Handles user queries with retrieval + memory."""
    result = conversation_chain({"question": user_input})
    return result["answer"]

def add_text_to_vector_db(text: str):
    """Add a custom text chunk into Chroma DB."""
    doc = Document(page_content=text)
    vectorstore.add_documents([doc])
    vectorstore.persist()

def add_file_to_vector_db(filepath: str):
    """Load a text file and store it in Chroma DB."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    add_text_to_vector_db(text)

# Quick test
if __name__ == "__main__":
    print("Bot ready. Type 'quit' to exit.")
    while True:
        query = input("You: ")
        if query.lower() in ["quit", "exit"]:
            break
        print("Bot:", chat_with_bot(query))
