# CodeChallenge: Machine Learning Engineer

## Project Overview
This project implements a Machine Learning solution for **product similarity matching** using Sentence Transformers. The goal is to find the most similar product descriptions for a given query. The project includes:
- A REST API for serving predictions.
- Containerization using Docker.
- CI/CD setup with GitHub Actions.
- A monitoring plan for deployed model.

---

## Features
1. **Model Serving**:
   - REST API implemented with Flask to serve predictions using Sentence Transformers.
   - Supports semantic similarity search for product descriptions.

2. **Containerization**:
   - Dockerized API for portability and consistent deployment.

3. **CI/CD**:
   - Automated pipeline with GitHub Actions to lint, test, and build Docker images.

4. **Monitoring**:
   - System metrics like system uptime, throughput, resource utilization.
   - Similarity metrics like Average similarity of top K results or hits, similarity score distribution and similarity thresholding.

---

## Technologies Used
- **Programming Language**: Python 3.9
- **Libraries**:
  - `sentence-transformers` for model inference.
  - `Flask` for API creation.
  - `Docker` for containerization.
- **Monitoring Tools which can be used (suggestions)**:
  - Prometheus + Grafana, mlflow
- **CI/CD**: GitHub Actions

---

## Setup Instructions

### Clone the Repository
To clone the repository, use the following commands:

```bash
git clone https://github.com/tarek-0566/CodeChallenge_ML_Engineer.git
cd CodeChallenge_ML_Engineer
```
# Flask Sentence Transformer API

## Create a Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate    # On Windows: myenv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the Flask API

Start the Flask server locally:

```bash
python flask_api.py
```

Access the endpoints:

- **Health Check:** [http://localhost:8000/health](http://localhost:8000/health)
- **Prediction:** [http://localhost:8000/predict](http://localhost:8000/predict)

### Example Prediction Request

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "query": ["What can I use to cut wood?"],
    "product_descriptions": [
        "Heavy-duty claw hammer with a non-slip grip handle.",
        "High-performance circular saw with laser guide."
    ]
}' http://localhost:8000/predict
```

## Run with Docker

### Build the Docker image:

```bash
docker build -t flask-sentence-transformer .
```

### Run the container:

```bash
docker run -p 8000:8000 flask-sentence-transformer
```

### Test the API:

- Use the `/health` endpoint to ensure the service is running.
- Send requests to `/predict` for predictions.

## CI/CD Pipeline

The CI/CD pipeline:

- Runs on all pushes and pull requests to the main branch.
- Steps include:
  - **Linting:** `flake8`
  - **Unit and integration tests:** `pytest`
  - **Docker image build and validation**

To verify the pipeline, check the **Actions** tab in the GitHub repository.

## Monitoring

### System Metrics:

- **System Uptime**
- **Throughput**
- **Latency**
- **Resource Utilization**

### Model Metrics:

- **Average Similarity of Top K results/hits**
- **Similarity Score Distribution**
- **Similarity Threshold**

## Folder Structure

```bash
CodeChallenge_ML_Engineer/
├── flask_api.py           # Flask API implementation
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── .github/
│   └── workflows/
│       └── main.yml       # CI/CD pipeline
├── monitoring_plan.md     # Monitoring plan documentation
├── tests/                 # Unit and integration tests
└── README.md              # Project documentation
```

## Enhancements for Full-Scale Production Setup

### **1. Model Versioning and Repository Support**
- **Purpose**: Managing multiple model versions and allow dynamic selection.
- **Implementation**:
  - Storing models in a versioned directory structure (e.g., `models/v1`, `models/v2`).
  - Adding an API endpoint (e.g., `/load-model`) to dynamically load models based on version.

### **2. Asynchronous Processing**
- **Purpose**: Improve throughput and responsiveness under high load.
- **Implementation**:
  - Using frameworks like **FastAPI** for async support.

### **3. Caching for Frequently Used Results**
- **Purpose**: Reduce redundant computations and improve performance.
- **Implementation**:
  - Using a caching system.
  - Checking the cache before running inference.

### **4. Monitoring and Logging**
- **Purpose**: Tracking application health and debug effectively.
- **Implementation**:
  - Integrating **Prometheus** and **Grafana** for monitoring API latency, error rates, and usage metrics.
  - Using structured logging log requests, responses, and errors.

### **5. Security Enhancements**
- **Purpose**: Protecting the application from unauthorized access and vulnerabilities.
- **Implementation**:
  - Using **API key authentication** or OAuth2 for access control.
  - Enforcing **HTTPS** for secure communication.

### **6. Horizontal Scaling**
- **Purpose**: Handling increased traffic by distributing load across multiple instances.
- **Implementation**:
  - Using **Docker** for containerization and **Kubernetes** for orchestration.
  - Add a load balancer to distribute incoming requests across instances.

### **7. Graceful Model Updates**
- **Purpose**: Ensuring uninterrupted service during model updates.
- **Implementation**:
  - Load new models in the background while keeping the current model active.
  - Provide an endpoint (e.g., `/switch-model`) to switch models seamlessly after validation.
  - Use version flags or environment variables for model selection.

