# CodeChallenge: Machine Learning Engineer

## Project Overview
This project implements a Machine Learning solution for **product similarity matching** using Sentence Transformers. The goal is to find the most similar product descriptions for a given query. The project includes:
- A REST API for serving predictions.
- Containerization using Docker.
- CI/CD setup with GitHub Actions.
- A monitoring plan for deployed models using MLflow.

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
   - Integrated MLflow for tracking metrics like latency, input drift, and similarity scores.

---

## Technologies Used
- **Programming Language**: Python 3.9
- **Libraries**:
  - `sentence-transformers` for model inference.
  - `Flask` for API creation.
  - `Docker` for containerization.
  - `MLflow` for monitoring and performance tracking.
- **CI/CD**: GitHub Actions

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/tarek-0566/CodeChallenge_ML_Engineer.git
cd CodeChallenge_ML_Engineer
```

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
python app.py
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
  - **Docker image build and validation`

To verify the pipeline, check the **Actions** tab in the GitHub repository.

## Monitoring

### System Metrics (Prometheus + Grafana):

- **API Latency**
- **Error Rate**
- **Request Volume**
- **Resource Usage (CPU, Memory)**

**Setup:**

- Install and configure Prometheus to scrape metrics from the Flask API.
- Use Grafana to visualize metrics with dashboards.

### Model Metrics (Evidently AI):

- **Input Data Drift**
- **Similarity Score Trends**

**Setup:**

- Use Evidently AI to monitor and compare the current input data distribution with the training data.

### Docker Monitoring (cAdvisor):

- **Track CPU, memory, and network usage of the Docker container.**

**Setup:**

- Install and run cAdvisor alongside the Docker container to collect resource usage statistics.

## Folder Structure

```bash
CodeChallenge_ML_Engineer/
├── app.py                 # Flask API implementation
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── .github/
│   └── workflows/
│       └── main.yml       # CI/CD pipeline
├── monitoring_plan.md     # Monitoring plan documentation
├── tests/                 # Unit and integration tests
└── README.md              # Project documentation
```

## Future Enhancements

- **Model versioning** using tools like DVC.
- **Autoscaling the API** using Kubernetes or Docker Swarm.
- **Advanced alerting** with Prometheus AlertManager.
