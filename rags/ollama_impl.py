from dotenv import load_dotenv

from langchain import chains
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.llms import Ollama
from langchain_ollama import OllamaEmbeddings

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders.text import TextLoader
from langchain_community.vectorstores import Chroma

import time


def init_chat_model(model):
    print("init_chat_mode")
    start = time.time()
    llm = Ollama(model=model)
    end = time.time()
    print("init_chat_mode: " + str(end - start))
    return llm


def get_embeddings(model):
    return OllamaEmbeddings(model=model)


def load_documents(materials):
    print("load_documents")
    start = time.time()

    documents = []
    for p in materials:
        if p.endswith('.pdf'):
            sf = time.time()
            pdf_loader = PyPDFLoader(p)
            ef = time.time()
            print("Loaded: " + p + " in " + str(sf-ef) + "s.")
            documents.extend(pdf_loader.load())
        elif p.endswith('.txt'):
            sf = time.time()
            txt_loader = TextLoader(p)
            ef = time.time()
            print("Loaded: " + p + " in " + str(sf-ef) + "s.")
            documents.extend(txt_loader.load())

    end = time.time()
    print("load_documents: " + str(end - start))
    return documents


def split_documents(documents, chunk_size, chunk_overlap):
    print("split_documents")
    start = time.time()
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size,
                                          chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(documents)
    end = time.time()
    print("split_documents: " + str(end - start))
    return texts


def create_vectorstore(texts, select_embedding):
    print("create_vectorstore")
    start = time.time()
    db = Chroma.from_documents(texts, select_embedding)
    end = time.time()
    print("create_vectorstore: " + str(end - start))
    return db


def create_retriever(db, search_type, num_docs):
    print("create_retriever")
    start = time.time()
    retriever = db.as_retriever(search_type=search_type,
                                search_kwargs={"k": num_docs})
    end = time.time()
    print("create_retriever: " + str(end - start))
    return retriever


def create_chain(llm, retriever, chain_type):
    chain = chains.RetrievalQA.from_chain_type(llm=llm,
                                               chain_type=chain_type,
                                               retriever=retriever,
                                               return_source_documents=True)
    return chain


class OllamaQA:
    def __init__(self, model, materials, chunk_size, chunk_overlap,
                 search_type, num_docs, chain_type):
        load_dotenv()
        self.llm = init_chat_model(model)
        self.select_embedding = get_embeddings(model)
        self.documents = load_documents(materials)
        self.texts = split_documents(self.documents, chunk_size, chunk_overlap)
        self.db = create_vectorstore(self.texts, self.select_embedding)
        self.retriever = create_retriever(self.db, search_type, num_docs)
        self.chain = create_chain(self.llm, self.retriever, chain_type)
