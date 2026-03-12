# semantic_matcher.py
import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

def semantic_similarity(text1, text2):
    """
    Returns similarity as percentage (0-100)
    """
    if not text1.strip() or not text2.strip():
        return 0.0

    emb1 = np.array(model.encode(text1)).reshape(1, -1)
    emb2 = np.array(model.encode(text2)).reshape(1, -1)

    score = cosine_similarity(emb1, emb2)[0][0]
    return float(score * 100)