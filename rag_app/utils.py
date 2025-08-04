from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from django.conf import settings  # ✅ Use Django settings

def process_document(file_path):
    print("Processing:", file_path)

    # Load PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)

    # Get key from Django settings
    openai_key = settings.OPENAI_API_KEY
    print("DEBUG: OpenAI key starts with:", openai_key[:8] if openai_key else "NOT SET")
    # print("API KEY:", repr(openai_key))

    if not openai_key:
        raise ValueError("OPENAI_API_KEY is not set. Check your .env or settings.py")

    # Use embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("vectorstore")
