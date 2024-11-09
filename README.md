# AI-Powered Recommender System with Data Pipelines and Cloud Deployment

This project is an end-to-end AI-powered recommender system that utilizes real-time data pipelines, machine learning, and cloud deployment to provide recommendations. It leverages FastAPI for the backend, Kafka and Spark for data processing, and AWS for cloud deployment. The recommender model is trained using collaborative filtering and served through an API to provide real-time product or content recommendations.

Table of Contents
1. Project Overview
2. Technologies Used
3. Architecture
4. Features
5. Installation
6. Usage
7. Project Structure
8. Deployment
9. Contributing
10. License



1. Project Overview
The AI-powered recommender system simulates a real-world scenario where user interaction data (e.g., clicks, purchases, ratings) is streamed in real-time. This data is processed through a Kafka-Spark pipeline and then used to make predictions using a machine learning model. The model serves recommendations through a FastAPI backend, and the entire project is deployed to AWS using Docker and ECS.



2. Technologies Used
Backend:
    FastAPI
    Python
Machine Learning:
    Scikit-learn
    TensorFlow
Data Engineering:
    Apache Kafka
    Apache Spark
    AWS Redshift
Cloud & DevOps:
    Docker
    AWS ECS (Elastic Container Service)
    AWS Lambda (optional for serverless architecture)
    Terraform (for Infrastructure as Code)



3. Architecture
This project is divided into three main components:
1) Data Pipeline:
    - Real-time user interaction data is streamed using Kafka.
    - Data is processed and cleaned using Apache Spark.
2) Machine Learning Model:
    - A collaborative filtering recommender model is trained using historical interaction data.
    -The model is deployed using FastAPI to serve real-time recommendations.
3) API & Cloud Deployment:
    - The FastAPI application exposes an API endpoint for retrieving product recommendations.
    - The application is containerized using Docker and deployed to AWS ECS for scalability and fault tolerance.



4. Features
- Real-time Data Processing: Stream and process user interaction data using Kafka and Spark.
- Recommendation System: Collaborative filtering model to recommend products based on user behavior.
- API for Recommendations: Exposes a /predict API endpoint to serve real-time recommendations.
- Cloud Deployment: Deployed on AWS using Docker and ECS, enabling a scalable and production-ready environment.
- MLFlow Integration: Tracks and manages machine learning experiments and models.



5. Installation
Prerequisites
- Python 3.8+
- Docker (for containerization)
- Kafka (for real-time streaming)
- Spark (for data processing)
- AWS Account (for cloud deployment)

Clone the Repository
    - git clone https://github.com/your-username/project-one-ai-recommender.git
    - cd project-one-ai-recommender

Setup Python Environment
1) Install the required Python packages:
pip install -r api/requirements.txt

2) Install Kafka and Spark:
Set Up Kafka
- Start Zookeeper:
    bin/zookeeper-server-start.sh config/zookeeper.properties
- Start Kafka Server:
    bin/kafka-server-start.sh config/server.properties
- Create a Kafka topic:
    bin/kafka-topics.sh --create --topic user-interactions --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1



6. Usage

1) Start the Data Pipeline
    - Kafka Producer: Simulate real-time user interactions (in data_pipeline/kafka_producer.py).
        python data_pipeline/kafka_producer.py
    - Kafka Consumer and Spark Processing: Start the Kafka consumer and Spark job to process the data.
        python data_pipeline/kafka_consumer.py
        python data_pipeline/spark_processing.py

2) Train the Model
    - Train the Recommender Model: Run the model training script to train and save the model.
        python model/train_model.py

3) Start the API
    - Run FastAPI Application: Start the FastAPI server for serving recommendations.
        uvicorn api.main:app --reload
    - Access API: The API will be running at http://localhost:8000.
    - API Endpoints:
        - /predict: Get recommendations based on user interaction data.



7. Project Structure

project-one-ai-recommender/
│
├── data_pipeline/                
│   ├── kafka_producer.py         
│   ├── kafka_consumer.py         
│   └── spark_processing.py       
│
├── model/                        
│   ├── train_model.py            
│   ├── model.pkl                 
│   └── recommender.py            
│
├── api/                          
│   ├── main.py                   
│   ├── requirements.txt          
│   ├── Dockerfile                
│   └── tests/                    
│       └── test_main.py          
│
├── config/                       
│   ├── kafka_config.yaml         
│   ├── aws_config.yaml           
│   └── app_config.yaml           
│
├── deployment/                   
│   ├── ecs_deploy.sh             
│   ├── terraform/                
│       └── ecs_setup.tf          
│
└── README.md                     



8. Deployment
Containerization
- Docker Build:
    docker build -t ai-recommender-app .
- Run Docker Container:
    docker run -p 8000:8000 ai-recommender-app

AWS ECS Deployment
1) Push Docker Image to AWS ECR:
    - Build, tag, and push the Docker image to an AWS Elastic Container Registry (ECR).
2) Deploy to AWS ECS:
    - Use the ecs_deploy.sh script to deploy the container to AWS ECS.
3) Terraform Setup:
    - Use the Terraform scripts in the deployment/terraform/ folder to set up AWS ECS infrastructure.


9. Contributing
Contributions are welcome! Please fork the repository and create a pull request for any bug fixes or new features.



10. License