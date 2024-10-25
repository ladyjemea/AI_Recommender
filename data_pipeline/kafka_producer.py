from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092', #connection to local kafka server
    value_serializer=lambda v: json.dumps(v).encode('utf-8') #convert data into json format
    )

#takes user data and sends it to the kafka topic
def send_to_kafka(action_data):
    producer.send('user-actions', action_data)
    producer.flush()
