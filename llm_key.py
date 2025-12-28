import os
from langchain_huggingface import HuggingFaceEmbeddings
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# Embedding model for vector DB
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Chat model setup
chat_model = InferenceClient("HuggingFaceH4/zephyr-7b-beta", token=HF_TOKEN)

print("Run Successful llm_key.py")
