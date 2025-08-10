import streamlit as st
from chatbot import chat_with_bot, add_text_to_vector_db
import base64

# ---------------- BACKGROUND IMAGE ---------------- #
def add_bg_with_overlay(bg_image_file):
    with open(bg_image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    tech_words = [
        "Agentic AI", "Gen AI", "Machine Learning",
        "LLM", "Vector Search", "Chatbot", "AI Agents",
        "Natural Language Processing", "Automation", "Deep Learning"
    ]

    # Random floating positions for words
    word_spans = "".join(
        [f"<span class='floating-word' style='top:{i*8}%; left:{(i*12)%90}%;'>{w}</span>"
         for i, w in enumerate(tech_words)]
    )

    css = f"""
    <style>
    /* Background */
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
        overflow: hidden;
    }}
    /* Floating tech words */
    .floating-word {{
        position: absolute;
        color: rgba(255, 255, 255, 0.15);
        font-size: 2rem;
        font-weight: bold;
        animation: float 20s linear infinite;
        white-space: nowrap;
    }}
    @keyframes float {{
        0% {{ transform: translateY(0px) translateX(0px); }}
        50% {{ transform: translateY(-20px) translateX(10px); }}
        100% {{ transform: translateY(0px) translateX(0px); }}
    }}
    /* Chat bubbles */
    .chat-bubble-user {{
        background: rgba(138, 43, 226, 0.7);
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 8px;
        max-width: 80%;
        align-self: flex-end;
    }}
    .chat-bubble-bot {{
        background: rgba(75, 0, 130, 0.7);
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 8px;
        max-width: 80%;
        align-self: flex-start;
    }}
    /* Responsive adjustments */
    @media (max-width: 768px) {{
        .floating-word {{
            font-size: 1.2rem;
        }}
    }}
    </style>
    {word_spans}
    """
    st.markdown(css, unsafe_allow_html=True)

# ---------------- APP UI ---------------- #
st.set_page_config(page_title=" Sasi Manchina's Assistant Bot - smabot : Techie AI Chatbot", layout="wide")

# Add background with tech words overlay
add_bg_with_overlay("image_vCjyiaev_1754762525531_raw.jpg")

st.markdown("<h1 style='color:#d6b3ff; text-shadow: 0 0 15px #a855f7;'>🤖 Agentic AI & Gen AI Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#e9d5ff;'>Powered by Machine Learning, Generative AI, and next-gen Vector Search 🚀</p>", unsafe_allow_html=True)

# ---------------- CHAT FUNCTIONALITY ---------------- #
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("💬 Ask me something Techy Techie:")

if st.button("Send"):
    if user_input.strip():
        bot_reply = chat_with_bot(user_input)
        st.session_state.history.append(("user", user_input))
        st.session_state.history.append(("bot", bot_reply))

# Display chat history
for role, text in st.session_state.history:
    if role == "user":
        st.markdown(f"<div class='chat-bubble-user'>{text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-bot'>{text}</div>", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ---------------- #
uploaded_file = st.file_uploader("📂 Upload a text file to add to my knowledge base:", type=["txt"])
if uploaded_file is not None:
    text_content = uploaded_file.read().decode("utf-8")
    add_text_to_vector_db(text_content)
    st.success("✅ File added to smabot memory!")
