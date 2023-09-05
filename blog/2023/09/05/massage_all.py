import quixstreams as qx
from quixstreams import StreamConsumer, EventData, CommitMode
import json
import click


def on_event_data_received_handler(stream: StreamConsumer, data: EventData):
    with data:
        payload = json.loads(data.value)
        payload["count"] *= 2
        
        message = qx.RawMessage(json.dumps(payload, indent=2).encode('utf-8'))
        message.key = str(payload["id"]).encode('utf-8')
        producer.publish(message)

        topic_consumer.commit()


def on_stream_received_handler(stream_received: StreamConsumer):
    stream_received.events.on_data_received = on_event_data_received_handler


def before_shutdown():
    print('before shutdown')    
    topic_consumer.dispose()
    producer.dispose()

@click.command()
def run_app():
    global client, topic_consumer, producer

    client = qx.KafkaStreamingClient('127.0.0.1:9092')

    topic_consumer = client.get_topic_consumer(
        topic="events",
        auto_offset_reset=qx.AutoOffsetReset.Earliest,
        consumer_group="events-consumer",
        commit_settings=CommitMode.Manual
    )
    producer = client.get_raw_topic_producer("massaged-events")

    print("Listening to streams. Press CTRL-C to exit.")

    topic_consumer.on_stream_received = on_stream_received_handler
    topic_consumer.subscribe()

    qx.App.run(before_shutdown=before_shutdown)

if __name__ == "__main__":
    run_app()