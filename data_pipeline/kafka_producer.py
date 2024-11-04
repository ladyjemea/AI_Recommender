from confluent_kafka import Producer

# Kafka producer configuration
conf = {'bootstrap.servers': "localhost:9092"}  # Kafka broker address
producer = Producer(**conf)

def delivery_report(err, msg):
    """ Delivery report handler called on successful or failed delivery of a message. """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def send_to_kafka(action_data):
    """ Send action data to Kafka """
    producer.produce('user-actions', key='key', value=str(action_data), callback=delivery_report)
    producer.flush()  # Ensure the message is delivered

## an example
#another examples