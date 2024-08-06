from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Define sentences
sentences = ["I love dogs", "I like dogs but not as much as cats"]

# Tokenize and get BERT embeddings
inputs = tokenizer(sentences, return_tensors='pt', padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)

# Get the mean of the output embeddings for each sentence
sentence_embeddings = outputs.last_hidden_state.mean(dim=1).numpy()

# Calculate cosine similarity
similarity = cosine_similarity([sentence_embeddings[0]], [sentence_embeddings[1]])[0][0]
print(f"Similarity: {similarity}")
