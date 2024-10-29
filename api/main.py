from fastapi import FastAPI
from pydantic import BaseModel
from data_pipeline.kafka_producer import send_to_kafka  # Import the Kafka producer

app = FastAPI()

# Define a Pydantic model for the expected JSON body
class UserAction(BaseModel):
    user_id: int
    product_id: int
    action: str

# The POST endpoint that will accept the JSON body
@app.post("/purchase")
def capture_user_action(action: UserAction):
    # Convert the Pydantic model to a dictionary and send to Kafka
    send_to_kafka(action.dict())
    return {"message": "User action recorded!"}