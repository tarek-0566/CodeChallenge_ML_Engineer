from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util

# Initialize Flask app
app = Flask(__name__)

# Load the SentenceTransformer model
model = SentenceTransformer("hkunlp/instructor-base")
print("Model loaded successfully!")


@app.route('/')
def home():
    return jsonify(
        {"message": "Welcome to the Sentence Transformer API!"}
    ), 200


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return jsonify(
            {"message": "This endpoint only supports POST requests. "
                        "Please send a POST request with a JSON body."}
        ), 405

    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract query and product descriptions
        query = data.get('query', [])
        product_descriptions = data.get('product_descriptions', [])

        if not query or not product_descriptions:
            return jsonify(
                {"error": "Both 'query' and 'product_descriptions' must "
                          "be provided."}
            ), 400

        # Embed query and product descriptions
        query_embedding = model.encode(query)
        product_embeddings = model.encode(product_descriptions)

        # Perform semantic search
        hits = util.semantic_search(
            query_embedding, product_embeddings, top_k=2
        )

        # Format results
        results = [
            {
                "product_description": product_descriptions[hit['corpus_id']],
                "score": round(hit['score'], 4)
            }
            for hit in hits[0]
        ]

        return jsonify({"query": query, "results": results}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
