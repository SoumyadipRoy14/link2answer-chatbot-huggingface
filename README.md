# 🎙️ Chatbot: Upload Link to Get Answer

A Retrieval-Augmented Generation (RAG) chatbot that extracts content from any webpage, stores it in a FAISS vector database, and answers user questions using Hugging Face-hosted LLMs. Designed for compliance-focused, context-grounded responses.

---

**#🚀 Features**

- 🔗 Accepts any public webpage URL
- 🧠 Extracts and cleans page content using BeautifulSoup
- 📚 Splits text into semantic chunks for vector storage
- 🔍 Retrieves relevant context using FAISS
- 🤖 Answers questions using Hugging Face's Zephyr-7B LLM
- 🔐 Secure token handling via `.env`
- 🧼 Cleans noisy dialogue markers and boilerplate text

---

**#🧰 Tech Stack**

| Component        | Tool/Library                          |
|------------------|---------------------------------------|
| Embeddings       | `sentence-transformers/all-MiniLM-L6-v2` via LangChain |
| Vector Store     | FAISS (CPU)                           |
| LLM              | `HuggingFaceH4/zephyr-7b-beta` via Hugging Face Hub |
| Web Scraping     | BeautifulSoup + Requests              |
| Prompting        | LangChain `ChatPromptTemplate`        |
| Environment Vars | `python-dotenv`                       |

---

**#📁 Project Structure**

chatbot-audio-to-answer/
│
├── llm_key.py          # Loads HF token, sets up embeddings + chat model
├── web_extract.py      # Scrapes and cleans webpage text
├── model.py                        # RAG pipeline: FAISS + prompt + chat model
├── requirements.txt        # Dependencies
├── .env                # Stores HF_TOKEN (not committed)
├── .gitignore          # Ignores .env, venv, pycache
└── README.md                      # You're reading it!

**#🔑 Hugging Face Setup**

1. Create an account at [huggingface.co](https://huggingface.co)
2. Go to [Settings → Access Tokens](https://huggingface.co/settings/tokens)
3. Create a token with **Inference permissions**
4. Create a `.env` file in your project root:
   ```env
   HF_TOKEN=hf_your_token_here

   
**#⚙️ Installation**

# Clone the repo
git clone https://github.com/soumya14/chatbot-audio-to-answer.git
cd chatbot-audio-to-answer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt


**#🧪 How to Use**

# Run the pipeline
python model.py

You’ll be prompted to:

Enter a URL (e.g. https://en.wikipedia.org/wiki/Sachin_Tendulkar)

Enter your question (e.g. "What is the birth place of Sachin Tendulkar?")

Get a grounded answer based on the page content

**#🧼 Cleaning Logic**

The system automatically removes:

Dialogue markers like Human:, User:, [/ASS]

Boilerplate like Subscribe, Advertisement, etc.

Truncated or irrelevant content

**#📌 Notes**
This project uses Hugging Face’s hosted LLMs via InferenceClient

Responses are grounded in retrieved context only

If the answer is not found, the model replies: "Not enough information."

**#📄 License**
This project is licensed under the MIT License. Feel free to fork, modify, and build upon it.

🙌 Credits
Built by Soumyadip  
Powered by LangChain, Hugging Face, and FAISS

