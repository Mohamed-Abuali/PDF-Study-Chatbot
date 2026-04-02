from langchain_community.document_loaders import PyPDFLoader



def load_pdf():
    loader = PyPDFLoader("./chapter2.pdf")
    docs = loader.load()
    return docs