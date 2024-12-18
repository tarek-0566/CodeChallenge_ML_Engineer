# Step 1: Use an official lightweight Python image as the base
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the application code into the container
COPY . .

# Step 5: Expose the port that Flask will run on
EXPOSE 8000

# Step 6: Command to run the Flask application
CMD ["python", "flask_api_1.py"]
