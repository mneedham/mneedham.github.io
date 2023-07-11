import quixstreams as qx
from quixstreams import StreamConsumer, EventData
import json

client = qx.KafkaStreamingClient('127.0.0.1:9092')

topic_consumer = client.get_topic_consumer(
    topic="events",
    auto_offset_reset=qx.AutoOffsetReset.Earliest,
    consumer_group="events-consumer-group"
)

def on_event_data_received_handler(stream: StreamConsumer, data: EventData):
    with data:
        payload = json.loads(data.value)        

        if payload["count"] > 500:
            with (producer := client.get_raw_topic_producer("big-events")):
                message = qx.RawMessage(json.dumps(payload, indent=2).encode('utf-8'))
                message.key = payload["uuid"].encode('utf-8')
                producer.publish(message)

def on_stream_received_handler(stream_received: StreamConsumer):
    stream_received.events.on_data_received = on_event_data_received_handler


print("Listening to streams. Press CTRL-C to exit.")

topic_consumer.on_stream_received = on_stream_received_handler
topic_consumer.subscribe()

qx.App.run()
