

# Step 1: Install dependencies (run in terminal)
# pip install -U langchain-community langchain-openai faiss-cpu pypdf tiktoken

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

import os

# 🔐 Set your OpenAI API key securely
os.environ["OPENAI_API_KEY"] = "your key"

# 🧾 Load your PDF
loader = PyPDFLoader("800xa.pdf")
documents = loader.load()

# ✂️ Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

# 🔍 Convert text chunks to vectors
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# 🔄 Setup the RetrievalQA pipeline
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4", temperature=0),
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
)

# ❓ Ask your question
query = "what is 800xa"
result = qa_chain(query)

print("Answer:", result["result"])
