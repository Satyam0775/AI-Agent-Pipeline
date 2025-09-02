import sys, os
import streamlit as st

# ---- Fix sys.path so "app" is always visible ----
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from app.weather_node import fetch_weather
from app.rag_node import load_pdf, rag_answer

st.set_page_config(page_title="🤖 AI Agent: Weather + PDF Q&A", layout="wide")

st.title("🤖 AI Agent: Weather + PDF Q&A")

# Sidebar: Mode selection
mode = st.sidebar.radio("Choose a mode:", ["🌦️ Weather", "📄 PDF Q&A", "🤖 Combined (Auto Detect)"])

# 🌦️ Weather Mode
if mode == "🌦️ Weather":
    st.header("🌦️ Weather Queries")
    city = st.text_input("Enter a city name:")
    if st.button("Get Weather"):
        if city:
            result = fetch_weather(city)
            st.success(result)
        else:
            st.warning("Please enter a city name.")

# 📄 PDF Mode
elif mode == "📄 PDF Q&A":
    st.header("📄 Ask Questions from PDF")

    if "pdf_loaded" not in st.session_state:
        st.session_state.pdf_loaded = False

    uploaded_pdf = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_pdf:
        with open("data/sample.pdf", "wb") as f:
            f.write(uploaded_pdf.read())
        load_pdf("data/sample.pdf")
        st.session_state.pdf_loaded = True
        st.success("✅ PDF loaded into Qdrant!")

    query = st.text_input("Ask something from the PDF:")
    if st.button("Search PDF"):
        if st.session_state.pdf_loaded:
            if query:
                answer = rag_answer(query)
                st.info(f"📄 Answer: {answer}")
            else:
                st.warning("Please enter a query.")
        else:
            st.warning("Upload and load a PDF first!")

# 🤖 Combined Mode (Decision Node)
elif mode == "🤖 Combined (Auto Detect)":
    from app.decision_node import decide_and_execute

    st.header("🤖 Combined Mode (Weather + PDF)")

    query = st.text_input("Ask me anything:")
    if st.button("Ask Agent"):
        if query:
            answer = decide_and_execute(query)
            st.success(answer)
        else:
            st.warning("Please enter a query.")
