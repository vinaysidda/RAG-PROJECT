import os
import shutil

VECTORSTORE_PATH = "vectorstore"  # Change this if your path is different

def reset_vectorstore():
    if os.path.exists(VECTORSTORE_PATH):
        try:
            shutil.rmtree(VECTORSTORE_PATH)
            print(f"✅ Vectorstore at '{VECTORSTORE_PATH}' has been deleted.")
        except Exception as e:
            print(f"❌ Error deleting vectorstore: {e}")
    else:
        print(f"⚠️ No vectorstore found at '{VECTORSTORE_PATH}'.")

if __name__ == "__main__":
    reset_vectorstore()

DOCUMENTS_PATH = "documents"

if os.path.exists(DOCUMENTS_PATH):
    for filename in os.listdir(DOCUMENTS_PATH):
        file_path = os.path.join(DOCUMENTS_PATH, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")
