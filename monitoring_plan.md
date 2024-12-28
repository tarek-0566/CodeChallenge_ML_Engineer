# Metrics to Track for Deployed for Semantic Search Model

## **1. System Metrics**

### **System Uptime**
- **Importance**: Ensures system reliability and availability.
- **Implementation**: Log uptime percentage and downtime frequency.

### **Throughput**
- **Importance**: Measures system's capacity to handle peak loads.
- **Implementation**: Log queries processed per second.

### **Resource Utilization**
- **Importance**: Monitors CPU, memory, GPU usage to optimize performance and cost.
- **Implementation**: 
  - Use tools like `nvidia-smi`, `Prometheus Node Exporter`.
  - Visualize in `Grafana` and set alerts for thresholds.

### **Latency**
- **Importance**: Low latency enhances user experience.
- **Implementation**: 
  - Log query processing times.
  - Monitor average, P95, P99 latencies via `Prometheus` and `Grafana`.
  - Set alerts for latency spikes.

## **2. Similarity Metrics**

### **Average Similarity of Top K results/hits**
- **Importance**: Measures how closely the top \( K \) recommendations align with the query, ensuring the model retrieves relevant results.
- **Implementation**:
  1. Use the Sentence Transformer to compute embeddings for queries and corpus.
  2. Retrieve top \( K \) recommendations based on similarity scores (e.g., cosine similarity).
  3. Calculate the average similarity score of these recommendations across all queries.

### **Similarity Score Distribution**
- **Importance**: Analyzes the range and consistency of similarity scores for top recommendations, ensuring reliable performance across queries.
- **Implementation**:
  1. Record similarity scores of the top \( K \) recommendations for all queries.
  2. Visualize the distribution of these scores using histograms or statistical plots.
  3. Identify anomalies or inconsistencies in the scores.

### **Similarity Thresholding**
- **Importance**: Ensures recommendations meet a minimum relevance standard by setting a similarity threshold.
- **Implementation**:
  1. Define a similarity threshold (e.g., \( 0.7 \)).
  2. Track the percentage of recommendations exceeding this threshold.
  3. Monitor trends in this metric to detect degradation in model relevance (e.g., declining **ThresholdPassRate**).

