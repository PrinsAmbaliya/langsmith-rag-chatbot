# LangSmith RAG Chatbot  

**Fully working RAG chatbot** jo LangSmith ki official documentation pe trained hai  
- Local embeddings → **Ollama (nomic-embed-text)**  
- Fast inference → **Groq (llama-3.3-70b)**  
- Real-time answers with perfect formatting & code blocks  

Live Demo (coming soon on Streamlit Cloud)

### Features
- Beautiful Markdown answers with code blocks
- Accurate answers only from official LangSmith docs
- Chat history (add kar sakta hai easily)
- Lightning fast responses (Groq power)

### How to run locally

```bash
# 1. Clone repo
git clone https://github.com/tera-username/langsmith-rag-chatbot.git
cd langsmith-rag-chatbot
```
```bash
# 2. Install dependencies
pip install streamlit langchain langchain-groq langchain-community faiss-cpu beautifulsoup4 python-dotenv
```
```bash
# 3. Add your Groq API key
echo "GROQ_API_KEY=your_groq_key_here" > .env
```
```bash
# 4. Make sure Ollama is running + model pulled
ollama serve
ollama pull nomic-embed-text
```
```bash
# 5. Run the app
streamlit run app.py
```
---
### Tech Stack

-Streamlit → UI

-Ollama → Local embeddings

-Groq → LLM (llama-3.3-70b)

-FAISS → Vector store

-LangChain → Everything else


---

### Screenshot


