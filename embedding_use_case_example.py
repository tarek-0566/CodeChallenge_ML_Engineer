from sentence_transformers import SentenceTransformer, util

#load model
model = SentenceTransformer("hkunlp/instructor-base")

# example query
query = ["What can I use to cut wood?"]

# example product descriptions
product_descriptions = [
    "Heavy-duty claw hammer with a non-slip grip handle for precise strikes.",
    "Durable 25ft tape measure with easy-lock and belt clip.",
    "High-torque ratchet screwdriver for efficient screwdriving. Stable screwdriving with 80-mm rod and magnetic bit holder.",
    "High-performance circular saw with laser guide for accurate cuts.",
    "Complete screwdriver set with durable magnetic heads for accuracy.",
    "Compact toolbox organizer with multiple compartments for easy storage."]

# embedd strings
query_embedding = model.encode(query)
product_embeddings = model.encode(product_descriptions)

# perform cosine similarity search
hits = util.semantic_search(query_embedding, product_embeddings, top_k=2)

# example result
print(f"Query: {query}")
for hit in hits[i]:
  print(f"  {corpus[hit['corpus_id']]} (Score: {round(hit['score'], 4)})")
  
