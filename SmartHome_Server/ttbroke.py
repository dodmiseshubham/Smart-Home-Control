from fastapi import FastAPI
import paho.mqtt.server as mqtt

app = FastAPI()
mqtt_broker = mqtt.MQTTServer()

@app.on_event("startup")
async def startup_event():
    mqtt_broker.start()  # Start the MQTT broker

@app.on_event("shutdown")
async def shutdown_event():
    mqtt_broker.stop()  # Stop the MQTT broker

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Client {client} connected with result code {rc}")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {msg.payload.decode('utf-8')}")

# Add MQTT callback functions to the broker
mqtt_broker.on_connect = on_connect
mqtt_broker.on_message = on_message

# Define FastAPI routes
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/publish/{topic}")
async def publish(topic: str, payload: str):
    mqtt_broker.publish(topic, payload)
    return {"topic": topic, "payload": payload}

@app.websocket("/subscribe")
async def subscribe(ws):
    await ws.accept()
    while True:
        msg = mqtt_broker.wait_message()
        await ws.send_text(f"{msg.topic} {msg.payload.decode('utf-8')}")
