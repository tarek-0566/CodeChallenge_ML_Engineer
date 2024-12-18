# Take home assignment

Welcome to the nexmart take home assignment for the Machine Learning Engineer (with MLOps) role.

nexMart as a company enables the digitalisation of the hardware and industrial supply sector by providing a comprehensive range of data services. To do so, a lot of external input data from producers and wholesalers needs to be ingested, transformed and delivered. One process step in this chain of operations is to handle the variety of formats and contents.

As the second step in the interview process, we kindly ask you to take on a coding assignment plus some related questions and submit it to us. 
For this, you will use a basic open source encoder referenced in the repo's embedding_use_case_example.py file. The model's task is to compare product descriptions with any given amount of queries, e.g. to find similar products and return the best suiting product descriptions. You can find out more about the model under this website: https://sbert.net/.
Your task is to deploy this model via a REST API, creating a CI/CD pipeline as well as taking care of the consequently occuring operational work. 
With this, we are looking to test your ability of 
1) deploying a machine learning model using containerization and
2) automating this deployment process using CI/CD (omit any orchestration for the exercise).
3) creating a plan for monitoring the model once it is deployed.

## Instructions:

- Create your own private project repo on GitHub to submit your solution once ready.
- Check out the embedding_use_case_example.py for how we imagine to use the model and inform yourself about the model.
- Containerize the model provided using Docker and create a working REST API for serving predictions.
- Set up a basic CI/CD pipeline that automatically builds and tests the model deployment.
- Write a brief explanation of what metrics you would track for the deployed model, why they are important, and how you would implement monitoring.
- Create any other files mentioned in the delivery expectation.
- Once you are satisfied with your solution, please give the nxcodingassignment GitHub user access to your repo and notify us (email below) about the submission.


## Tools Required:

- API: Python code & packages for API creation.
- Docker: For containerizing the model API.
- CI/CD Tool: OS tool like GitHub Actions or GitLab CI.
  

## Delivery expectations:

1) Model Deployment (Containerization):
- A working Dockerfile (and optionally docker-compose files) for containerizing the model API.
- Source code for serving the model via the API and any tests you deem necessary.

2) CI/CD Setup:
- a CI/CD pipeline configuration (e.g., .github/workflows/ or .gitlab-ci.yml).

3) Monitoring Plan:
- A clear & concise document that describes your monitoring strategy.

4) A README of the solution submitted with
   
   a. instructions on how to build & run your solution locally.
   
   b. any API & CI/CD pipeline documentation you deem useful.
   
   c. a few explanations on which additional code you could have written to make it a full-scale production setup with a model repository containing various model versions.
   
   d. anything else that you would like to let us know with regards to the assignment like explanations, additional info etc if any. (not mandatory)


Generally, as this is a selection process exercise, we do not not expect a full-blown solution to save the candidate’s time. That being said, it is important for us to see notions to evaluate the seniority of the candidate which means we expect code in basic production quality (not MVP standard) and minimal testing that your code works & checking the most important aspects of the task. Evaluation criteria include the compliance with the delivery expectations, logical thinking, code and documentation quality.

Any technical questions regarding the assignment can be submitted to this email address: coding.assignment@nexmart.com. For all other questions, please refer to your recruiter contact.
