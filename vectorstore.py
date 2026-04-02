from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
import os

embedd = OllamaEmbeddings(model="mxbai-embed-large")


vector_location = "./chroma_langchain_db"

add_document = not os.path_ex
