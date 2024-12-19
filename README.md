# CodeChallenge: Machine Learning Engineer

## Project Overview
This project implements a Machine Learning solution for **product similarity matching** using Sentence Transformers. The goal is to find the most similar product descriptions for a given query. The project includes:
- A REST API for serving predictions.
- Containerization using Docker.
- CI/CD setup with GitHub Actions.
- A monitoring plan for deployed models using Prometheus + Grafana, Evidently AI, and Docker monitoring tools.

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
   - System metrics like latency, errors, and resource usage tracked using Prometheus + Grafana.
   - Model performance metrics (e.g., data drift) tracked using Evidently AI.
   - Docker container resource usage monitored with cAdvisor.

---

## Technologies Used
- **Programming Language**: Python 3.9
- **Libraries**:
  - `sentence-transformers` for model inference.
  - `Flask` for API creation.
  - `Docker` for containerization.
- **Monitoring Tools**:
  - Prometheus + Grafana
  - Evidently AI
  - Docker monitoring tools (cAdvisor)
- **CI/CD**: GitHub Actions

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/tarek-0566/CodeChallenge_ML_Engineer.git
cd CodeChallenge_ML_Engineer
```

### Setting Up a Virtual Environment

To create and activate a virtual environment, follow these steps:

```bash
python -m venv myenv
source myenv/bin/activate    # On Windows: myenv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Start the Flask Server Locally
```bash
python app.py
```

### Access the Endpoints
- **Health Check**: [http://localhost:8000/health](http://localhost:8000/health)
- **Prediction**: [http://localhost:8000/predict](http://localhost:8000/predict)

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

### Build the Docker Image
```bash
docker build -t flask-sentence-transformer .
```

### Run the Container
```bash
docker run -p 8000:8000 flask-sentence-transformer
```

### Test the API
- Use the `/health` endpoint to ensure the service is running.
- Send requests to `/predict` for predictions.

## CI/CD Pipeline

The CI/CD pipeline runs on all pushes and pull requests to the main branch and includes the following steps:

1. **Linting**: Code quality checks using `flake8`.
2. **Unit and Integration Tests**: Tests executed with `pytest`.
3. **Docker Image Build and Validation**: Ensures the Docker image is correctly built.

### Checking the Pipeline
- Navigate to the **Actions** tab in the GitHub repository to verify pipeline runs.

## Monitoring

### System Metrics (Prometheus + Grafana)

Key metrics:
- API Latency
- Error Rate
- Request Volume
- Resource Usage (CPU, Memory)

#### Setup:
1. Install and configure Prometheus to scrape metrics from the Flask API.
2. Use Grafana to visualize metrics with pre-built dashboards.

### Model Metrics (Evidently AI)

Key metrics:
- Input Data Drift
- Similarity Score Trends

#### Setup:
1. Use Evidently AI to monitor and compare the current input data distribution with the training data.

### Docker Monitoring (cAdvisor)

Track CPU, memory, and network usage of the Docker container.

#### Setup:
1. Install and run cAdvisor alongside the Docker container to collect resource usage statistics.

## Folder Structure
```bash
CodeChallenge_ML_Engineer/
├── flask_api_1.py          # Flask API implementation
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

1. **Model Versioning**: Implement version control for the model using tools like DVC.
2. **Autoscaling**: Use Kubernetes or Docker Swarm to scale the API dynamically based on load.
3. **Advanced Alerting**: Configure Prometheus AlertManager for proactive notifications based on predefined thresholds.


