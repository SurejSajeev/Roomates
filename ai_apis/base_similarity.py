import spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Try to load the English language model, if not installed, download it
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading language model for the spaCy POS tagger")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    # Convert to lowercase and remove punctuation
    doc = nlp(text.lower())
    return " ".join([token.text for token in doc if not token.is_punct])

def get_embedding(text):
    # Get the document vector (average of word vectors)
    doc = nlp(text)
    return doc.vector

def similarity(statement1, statement2):
    # Preprocess the statements
    proc_stmt1 = preprocess(statement1)
    proc_stmt2 = preprocess(statement2)
    
    # Get embeddings
    emb1 = get_embedding(proc_stmt1)
    emb2 = get_embedding(proc_stmt2)
    
    # Reshape embeddings for cosine similarity calculation
    emb1 = emb1.reshape(1, -1)
    emb2 = emb2.reshape(1, -1)
    
    # Calculate cosine similarity
    sim_score = cosine_similarity(emb1, emb2)[0][0]
    
    return sim_score

# Example usage
statement1 = "i like dogs."
statement2 = "i dont like dogs, but I like cats"

similarity_score = similarity(statement1, statement2)
print(f"Similarity score: {similarity_score:.4f}")