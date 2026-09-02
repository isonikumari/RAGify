import hashlib
import os
from functools import lru_cache

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

CHROMA_DIR = os.path.abspath("vector_db")
COLLECTION_NAME = "meeting_transcript"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-MiniLM-L6-v2"


@lru_cache(maxsize=2)
def get_embeddings():
  return HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL,
    model_kwargs={"device": 'cpu'}
  )


def get_collection_name(transcript: str | None = None) -> str:
  if transcript is None:
    return COLLECTION_NAME

  digest = hashlib.sha256(transcript.strip().encode("utf-8")).hexdigest()[:12]
  return f"{COLLECTION_NAME}_{digest}"


def build_vector_store(transcript: str, collection_name: str | None = None) -> Chroma:
  print("Building vector store")
  collection_name = collection_name or get_collection_name(transcript)

  splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
  )
  chunks = splitter.split_text(transcript)

  docs = [Document(page_content=chunk, metadata={'chunk_index': i})
          for i, chunk in enumerate(chunks)]

  embeddings = get_embeddings()
  vector_store = Chroma.from_documents(
      documents=docs,
      embedding=embeddings,
      collection_name=collection_name,
      persist_directory=CHROMA_DIR
  )

  return vector_store


def load_vector_store(collection_name: str | None = None) -> Chroma:
  embeddings = get_embeddings()
  collection_name = collection_name or COLLECTION_NAME
  vector_store = Chroma(
      embedding_function=embeddings,
      collection_name=collection_name,
      persist_directory=CHROMA_DIR
  )
  return vector_store


def ensure_vector_store(transcript: str, collection_name: str | None = None) -> Chroma:
  collection_name = collection_name or get_collection_name(transcript)
  try:
    vector_store = load_vector_store(collection_name)
    vector_store.get(limit=1)
    return vector_store
  except Exception:
    return build_vector_store(transcript, collection_name)


def get_retriever(vector_store: Chroma, k: int = 10):
  return vector_store.as_retriever(
    search_kwargs={"k": k}
  )




