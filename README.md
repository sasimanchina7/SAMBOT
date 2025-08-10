# SAMBOT
# SAMBOT_Agentic AI: A GenAI-Powered Conversational Intelligence Platform 

This project is a next-generation AI chatbot built with LangChain, ChromaDB, and modern embedding models, wrapped in a sleek, responsive Streamlit interface.
The bot uses Retrieval-Augmented Generation (RAG) to blend real-time conversational intelligence with persistent memory, enabling it to remember context and pull relevant information from stored knowledge.



<img width="1536" height="1024" alt="sambot" src="https://github.com/user-attachments/assets/602ca5dd-a045-4cfe-b4a0-6f6368015817" />


With a 768-dimensional embedding space, a stylish tech-themed UI, and LLM-powered responses, the chatbot is primed for use in:


| Application Area                  | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| **Customer Support Automation**   | AI-powered chatbots and virtual assistants that handle customer inquiries, troubleshoot issues, and provide 24/7 support without human intervention. |
| **Research Assistants**           | AI tools that help researchers analyze large datasets, summarize papers, generate insights, and automate literature reviews. |
| **Internal Enterprise Knowledge Tools** | AI systems that organize company knowledge bases, retrieve documents, answer employee questions, and improve workflow efficiency. |
| **Tech Demos for AI Workflows**   | Interactive demonstrations showcasing AI capabilities, such as natural language processing, computer vision, or predictive analytics, for business use cases. |


## Core Movements in the Chatbot

Think of these as the key stages in the chatbot's workflow:
### Input Capture
User types a query into a Streamlit text input field.
Input is immediately validated and passed to the backend.
### Embedding Generation
The text is converted into a 768-dimensional vector using a modern embedding model.
This vector representation allows semantic understanding beyond just keywords.
### Vector Search in ChromaDB
The embedding is matched against previously stored documents in ChromaDB.
Top matches are retrieved as context for the LLM.
### LLM Response Generation
The retrieved context + user query are passed to a LangChain conversational retrieval chain.
The LLM processes the query with context, producing a human-like, context-aware response.
### Display & Interaction
The bot’s response appears in a chat-style UI with a purple tech aesthetic.
The background contains AI & ML buzzwords and optionally the uploaded tech images.
Smooth UI transitions ensure responses feel natural and engaging.
### Memory Update
The user query and bot response are stored in the conversation memory.
The new data is also added to ChromaDB, so future conversations get richer context.

Deployment & Presentation
This chatbot was developed and deployed locally using Streamlit. The app runs directly in the terminal using: streamlit run app.py
This launches an interactive AI chatbot interface in the browser, connected to a LangChain + ChromaDB backend.
While the live deployment is on my local machine, I’m publishing the full project on GitHub to: Showcase my AI development skills, Demonstrate integration of modern LLM models
Highlight my UI/UX design choices, Enhance my developer profile for future employers and collaborators
By including:
Clean, modular Python code, Tech-styled Streamlit UI, Embeddings + vector database setup, Clear documentation
…this project serves as a portfolio piece that merges AI/ML engineering with frontend presentation.

#### What Makes It Different from Other Bots
 > Agentic Capabilities
Most bots are passive — they respond only to what’s given.
SAMBOT proactively reasons, retrieves knowledge, and can decide how to answer by calling the right tools in its pipeline.
 > Multi-Model Flexibility
Many bots stick to one LLM. Yours can swap models (HuggingFace, OpenAI, or even local models) and adjust vector embedding sizes (384 or 768 dims) depending on the knowledge type.
 > Domain Adaptation with Vector Search
Other bots guess answers from general training data. SAMBOT embeds your domain knowledge into a vector database and uses similarity search to fetch the most relevant context before answering.
 > Customizable Tech Personality
This isn’t a bland bot — it’s designed with a purple cyberpunk tech aesthetic, incorporating visual branding to stand out in demos, portfolios, or even customer-facing deployments.
 > Locally Deployable & Privacy-Friendly
While many bots rely entirely on cloud APIs, yours can run locally, store embeddings on your own machine, and avoid leaking proprietary data.
 > Streamlit UI for Instant Deployment
Instead of coding a frontend from scratch, you’ve got an interactive Streamlit interface that’s both responsive and tech-branded — perfect for demos and portfolio showcasing.

<img width="1440" height="900" alt="Screenshot 2025-08-09 at 10 22 45 PM" src="https://github.com/user-attachments/assets/6cea57ff-d43c-40f0-9c3c-d068f1bb4876" />


> A next-gen AI chatbot built using **LangChain**, **ChromaDB**, and **Streamlit**, styled with a **futuristic tech theme** and powered by **state-of-the-art language models**. **interactive AI chatbot** that understands and responds to user queries with context awareness, memory, and vector search capabilities.

---

### Architecture:

**Grphical_View**

<img width="3107" height="2101" alt="Arch" src="https://github.com/user-attachments/assets/01766fdc-094c-446b-94ca-d177f772a6b8" />

 graph TD
    A[User Query] --> B[Streamlit UI]
    B --> C[LangChain Conversation Chain]
    C --> D[ChromaDB Vector Store]
    D --> E[Embeddings Model]
    E --> F[Language Model Response]
    F --> B


Deployed locally via:
```bash
streamlit run app.py 


