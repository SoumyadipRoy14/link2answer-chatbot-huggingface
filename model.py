# pip install langchain langchain-community langchain-text-splitters faiss-cpu beautifulsoup4 requests langchain-huggingface python-dotenv

import re
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

from llm_key import embedding_model, chat_model
import web_extract  

# 1) Prepare text and metadata
raw_text = web_extract.text_content or ""
source_url = web_extract.url

if not raw_text.strip():
    raise ValueError("No text extracted from the provided URL. Please check the URL or extraction logic.")

# 2) Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.create_documents([raw_text], metadatas=[{"source": source_url}])

# 3) Build FAISS vector store and retriever
vectorstore = FAISS.from_documents(documents, embedding_model)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 4) Prompt template for grounded answers
prompt = ChatPromptTemplate.from_template(
    "You are a compliance-focused assistant.\n"
    "Answer ONLY the user's question using the provided context.\n"
    "Do not repeat or invent questions from the context.\n"
    "If the answer is not present, reply: 'Not enough information.'\n\n"
    "Source: {source}\n\n"
    "Context:\n{context}\n\n"
    "Question: {question}\n"
    "Answer:"
)

# 5) RAG pipeline function
def ask_question(query: str) -> str:
    # Retrieve relevant docs
    retrieved_docs = retriever.invoke(query)

    # Build context
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)
    source = source_url if source_url else "Unknown"

    # Call chat model
    response = chat_model.chat_completion(
        messages=[
            {"role": "system", "content": "You are a compliance-focused assistant."},
            {"role": "user", "content": prompt.format(context=context, question=query, source=source)}
        ],
        max_tokens=800
    )

    # Print sources
    print("Top sources:")
    for i, d in enumerate(retrieved_docs, 1):
        print(f"- {i}. {d.metadata.get('source', 'Unknown')}")

    # Extract and clean answer
    answer = response.choices[0].message["content"].strip()
    answer = re.sub(r"(Human:|User:|\[/ASS\]).*", "", answer)
    
    if "Answer:" in answer:
        answer = answer.split("Answer:")[-1].strip()

    print("Answer:", answer)

    # Handle truncation
    if response.choices[0].finish_reason == "length":
        followup = chat_model.chat_completion(
            messages=[{"role": "user", "content": "Please continue your last answer."}],
            max_tokens=300
        )
        answer += " " + followup.choices[0].message["content"].strip()

    return answer

# 6) Quick tests
if __name__ == "__main__":
    question = input("Enter your question: ")
    print("A:", ask_question(question))

print("Run Successful model.py")
