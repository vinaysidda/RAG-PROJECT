# from langchain_community.document_loaders import TextLoader
# laoder = TextLoader('text.txt')
# text_document = laoder.load()
# print(text_document)


# from langchain_community.document_loaders import PyPDFLoader
# Loader = PyPDFLoader('kubernetes.pdf')
# text_document = Loader.load()
# print(text_document)

# from langchain_community.document_loaders import WebBaseLoader
# import bs4
# import os
# os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

# loader = WebBaseLoader(web_paths=["https://mrunal.org/2024/08/global-warming-flawed-idea-economic-survey-2024.html"],
#     bs_kwargs=dict(
#         parse_only=bs4.SoupStrainer(
#             class_=["post-title", "post-content", "post-header"]
#         )
#     ),) 
# # you can give many webpaths, it will load all of them if you do not give comma then ther will be an error 
# HTMl_document = loader.load()
# print(HTMl_document)


# from langchain_community.document_loaders import TextLoader
# def loadtext():
#     loader = TextLoader('text.txt')
#     text_document = loader.load()
#     print(text_document)
# if __name__ == "__main__":
#     loadtext()

# from langchain_community.document_loaders import ArxivLoader
# docs = ArxivLoader(query="1605.08386", load_max_docs=2).load()
# # docs.load()
# # print(len(docs))
# print(docs[0])



# from langchain_community.document_loaders import WikipediaLoader
# docs = WikipediaLoader(query="kannada movies", load_max_docs=2).load()
# # len(docs)
# # print(docs)

# from langchain_text_splitters import RecursiveCharacterTextSplitter
# text_splitter = RecursiveCharacterTextSplitter(chunk_size= 500,chunk_overlap = 50)


# final_document = text_splitter.split_documents(docs)
# print(final_document[1])

# from langchain_community.document_loaders import TextLoader
# loader = TextLoader("text.txt")
# text_document = loader.load()

from langchain_text_splitters import RecursiveCharacterTextSplitter
# text_splitter = RecursiveCharacterTextSplitter(chunk_size= 100,chunk_overlap =20)
speech =""
with open("text.txt") as f:
    speech = f.read()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size =100, chunk_overlap=20)
    final_document = text_splitter.split_documents([speech])
    print(final_document[0])
    print(type(final_document))


