# LangSmith RAG Chatbot  

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

- Streamlit → UI

- Ollama → Local embeddings

- Groq → LLM (llama-3.3-70b)

- FAISS → Vector store

- LangChain → Everything else


---

### Screenshot

1. When vector store for the first time:
<img width="1920" height="1080" alt="Screenshot (342)" src="https://github.com/user-attachments/assets/75c0e705-f0b1-4c03-893c-7722046bdddc" />

2. When vector store ready:
<img width="1920" height="1080" alt="Screenshot (343)" src="https://github.com/user-attachments/assets/402f4847-c13a-40e2-8c51-03fc69e299e8" />

3. Now final output:
<img width="1920" height="1080" alt="Screenshot (344)" src="https://github.com/user-attachments/assets/82352a47-caeb-419d-8d3a-e7c1fa62f665" />

