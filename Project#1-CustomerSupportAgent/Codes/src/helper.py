import faiss
import numpy as np
import pandas as pd
from typing import Tuple, List
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from google import genai
from google.genai import types

def create_embeddings(df: pd.DataFrame, column_name: str, api_key: str, model: str = "text-embedding-004") -> np.ndarray:
    embeddings = GoogleGenerativeAIEmbeddings(
        google_api_key=api_key.strip(),
        model=model,
        task_type="retrieval_document"
    )
    texts = df[column_name].tolist()
    vectors_list = embeddings.embed_documents(texts)
    return np.array(vectors_list).astype('float32')

def create_index(vectors: np.ndarray, index_file_path: str) -> faiss.Index:
    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)
    faiss.write_index(index, index_file_path)
    return index

def semantic_similarity(query: str, index: faiss.Index, api_key: str, model: str = "text-embedding-004", k: int = 3) -> Tuple[np.ndarray, np.ndarray]:
    embeddings_model = GoogleGenerativeAIEmbeddings(
        google_api_key=api_key.strip(), 
        model=model,
        task_type="retrieval_query" 
    )
    query_vector = embeddings_model.embed_query(query)
    query_vector = np.array([query_vector]).astype('float32')
    distances, indices = index.search(query_vector, k)
    return distances, indices

def call_llm(query: str, responses: List[str], api_key: str, model_name: str) -> str:
    client = genai.Client(api_key=api_key.strip())
    context_text = "\n".join([f"- {r}" for r in responses])
    
    system_instruction = (
        "You are a professional customer support assistant. "
        "Use provided context only. If unsure, ask for help."
    )
    
    prompt = f"Context: {context_text}\n\nQuery: {query}\n\nProvide Urgency (1-5), Category, and Response."

    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.0
        )
    )
    return response.text