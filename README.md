# 🤖 AI  Pipeline

## 📌 Objective
Develop a simple AI pipeline using **LangChain**, **LangGraph**, and **LangSmith** to demonstrate an understanding of embeddings, vector databases, Retrieval-Augmented Generation (RAG), and clean coding practices.

---

## 📋 Assignment Requirements
The candidate must:

- Use **LangGraph** to implement an agentic pipeline with two functionalities:  
  - Fetch real-time weather data using the **OpenWeatherMap API**.  
  - Answer questions from a **PDF document** using RAG (Retrieval-Augmented Generation).  
- Implement a **LangGraph node** that decides whether to call the weather API or fetch information from the PDF.  
- Process the fetched data using a **Large Language Model (LLM)** via LangChain.  
- Generate embeddings for the processed data and store them in a **vector database (Qdrant)**.  
- Implement a **RAG-based query mechanism** to retrieve and summarize stored information.  
- Evaluate the LLM’s response using **LangSmith**.  
- Write **test cases** for API handling, LLM processing, and retrieval logic while maintaining clean, modular code.  
- Create a **UI interface** using Streamlit to demonstrate the application using a simple chat interface.  

---

## 📦 Deliverables
- 🐍 Python code in a GitHub repository  
- 📄 README.md with setup instructions and implementation details  
- 📊 LangSmith logs/screenshots showcasing LLM response evaluation  
- 🧪 Test results from unit tests  
- 💻 Streamlit UI demo  
- 🎥 Loom video explaining LangSmith results and the code  

---

## 📝 Evaluation Criteria
- ✔ Correct integration of **LangGraph** and **LangChain**  
- ✔ Proper decision-making within LangGraph nodes  
- ✔ Working vector database storage and retrieval  
- ✔ Effective LangSmith evaluation  
- ✔ Clean, well-structured, and well-tested code  
- ✔ Functional and user-friendly **Streamlit UI**  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/ai-pipeline-assignment.git
cd ai-pipeline-assignment

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate   # Mac/Linux

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in the project root:

# Weather
OPENWEATHERMAP_API_KEY=your_openweather_key_here

# HuggingFace
HUGGINGFACEHUB_API_TOKEN=your_huggingface_key_here

# LangSmith
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=ls__xxxxxxxxxxxxxxxxxxxx
LANGSMITH_PROJECT=AI_Agent_Assignment
LANGSMITH_ENDPOINT=https://api.smith.langchain.com

5️⃣ Start Qdrant (Vector DB)
docker run -p 6333:6333 qdrant/qdrant

6️⃣ Run Streamlit App
streamlit run ui/streamlit_app.py

🧪 Running Tests
pytest -v


✅ All tests should pass.

📊 LangSmith Evaluation

Our pipeline is instrumented with LangSmith for tracing and evaluation.

1. Weather Query Run

Input:

What is the weather in Delhi?


Output:

🌦️ The current temperature in Delhi, IN is 24.74°C with overcast clouds.

2. PDF Query Run

Input:

What are the deliverables of the assignment?


Output:

AI Task  
Deliverables include Python code in GitHub, README.md, LangSmith logs/screenshots, test results, Streamlit demo, and Loom video.

🗂️ Project Structure
ai_pipeline_assignment/
│── app/                  # Core pipeline logic
│   ├── config.py
│   ├── decision_node.py
│   ├── llm_node.py
│   ├── main.py
│   ├── pipeline.py
│   ├── rag_node.py
│   ├── vectorstore.py
│   └── weather_node.py
│
│── data/                 # Sample PDFs / data
│── tests/                # Unit tests
│── ui/                   # Streamlit app
│   └── streamlit_app.py
│── docs/                 # Screenshots (LangSmith logs)
│   ├── langsmith_weather.png
│   └── langsmith_pdf.png
│── .env                  # API keys 
│── requirements.txt
│── README.md


✨ Thank You!
