from sentence_transformers import SentenceTransformer, util

#load model
model = SentenceTransformer("./models/instructor-base")

# example query
query = ["What can I use to cut?"]	

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
hits = util.semantic_search(query_embedding, product_embeddings, top_k=3)

# # example result
# print(f"Query: {query}")    ## this section is giving a Name Error: name 'i' is not defined
# for hit in hits[i]:
#   print(f"  {corpus[hit['corpus_id']]} (Score: {round(hit['score'], 4)})")

# A New for loop is written to print all hits
for hit_group in hits:
    results = [
        {
            "product_description": product_descriptions[hit['corpus_id']],
            "score": round(hit['score'], 4)
        }
        for hit in hit_group
    ]
    print(results)
