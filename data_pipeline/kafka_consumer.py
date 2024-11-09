from confluent_kafka import Consumer, KafkaException, KafkaError

# Kafka consumer configuration
conf = {
    'bootstrap.servers': "localhost:9092",
    'group.id': "mygroup",
    'auto.offset.reset': 'earliest'
}

# Create Consumer instance
consumer = Consumer(conf)

# Subscribe to the topic
consumer.subscribe(['user-actions'])

# Process messages
def consume_messages():
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"End of partition reached {msg.topic()} {msg.partition()} {msg.offset()}")
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(f"Received message: {msg.value().decode('utf-8')} from {msg.topic()}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_messages()