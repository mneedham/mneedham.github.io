import quixstreams as qx
from quixstreams import StreamConsumer, EventData, CancellationTokenSource, CommitMode
import time
import json
import sys
import threading
import click

def on_event_data_received_handler(stream: StreamConsumer, data: EventData):
    global events_consumed
    with data:
        payload = json.loads(data.value)
        payload["count"] *= 2
        
        message = qx.RawMessage(json.dumps(payload, indent=2).encode('utf-8'))
        message.key = str(payload["id"]).encode('utf-8')
        producer.publish(message)

        topic_consumer.commit()

        with thread_lock:
            events_consumed += 1

        if events_consumed >= events_to_consume:
            if not cancellation_thread.is_alive():
                cancellation_thread.start()
                print("Cancellation token triggered")
            return


def on_stream_received_handler(stream_received: StreamConsumer):
    stream_received.events.on_data_received = on_event_data_received_handler


def before_shutdown():
    print('before shutdown')    
    topic_consumer.dispose()
    producer.dispose()

@click.command()
@click.option('--number-events', default=1)
def run_app(number_events):
    global client, topic_consumer, producer
    global events_to_consume, events_consumed, thread_lock, cancellation_thread
    
    client = qx.KafkaStreamingClient('127.0.0.1:9092')

    topic_consumer = client.get_topic_consumer(
        topic="events",
        auto_offset_reset=qx.AutoOffsetReset.Earliest,
        consumer_group="events-consumer",
        commit_settings=CommitMode.Manual
    )
    producer = client.get_raw_topic_producer("massaged-events")

    thread_lock = threading.Lock()
    cts = CancellationTokenSource()
    cancellation_thread = threading.Thread(target=lambda: cts.cancel())

    events_to_consume = number_events
    events_consumed = 0

    print("Listening to streams. Press CTRL-C to exit.")

    topic_consumer.on_stream_received = on_stream_received_handler
    topic_consumer.subscribe()

    qx.App.run(cts.token, before_shutdown=before_shutdown)
    if cancellation_thread.is_alive():
        cancellation_thread.join()  



if __name__ == "__main__":
    run_app()