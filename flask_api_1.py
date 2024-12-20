from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util

# Initialize Flask app
app = Flask(__name__)

# Load the SentenceTransformer model
# model = SentenceTransformer("./models/instructor-base")
model = SentenceTransformer("hkunlp/instructor-base")
print("Model loaded successfully!")


@app.route('/')
def home():
    return jsonify(
        {"message": "Welcome to the Sentence Transformer API!"}
    ), 200


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    queries = data.get('queries', [])
    product_descriptions = data.get('product_descriptions', [])

    if not queries or not product_descriptions:
        return jsonify(
            {"error": "Queries and product descriptions are required"}
        ), 400

    # Encode queries and product descriptions
    query_embeddings = model.encode(
        queries, convert_to_tensor=True
    )
    product_embeddings = model.encode(
        product_descriptions, convert_to_tensor=True
    )

    # Compute cosine similarities
    hits = util.semantic_search(
        query_embeddings, product_embeddings
    )

    results = []
    for hit_group in hits:
        result = [
            {
                "product_description": product_descriptions[
                    hit['corpus_id']
                ],
                "score": round(hit['score'], 4)
            }
            for hit in hit_group
        ]
        results.append(result)

    return jsonify(results), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
