from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
import os
from loader import load_pdf

embedd = OllamaEmbeddings(model="mxbai-embed-large")


vector_location = "./chroma_langchain_db"

add_document = not os.path.exists(vector_location)
def get_data():
    data =[]
    if add_document:
        docs = load_pdf()
        documents=[]
        ids=[]
        for i in docs:
            documents.append(i.page_content)
        data = documents
    return data



