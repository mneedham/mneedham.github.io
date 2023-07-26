import datetime, random, uuid

from confluent_kafka import Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import (
    SerializationContext,
    MessageField,
)
schema_registry_conf = {'url': 'http://localhost:8081'}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

with open("telemetry.avsc") as f:
    value_schema = f.read()
avro_serializer = AvroSerializer(schema_registry_client, value_schema)

producer_conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(producer_conf)

user_countries = ["US", "IN", "GB", "CA", "AU", "DE", "FR", "IT", "BR", "JP"]
resolutions = ["480p", "720p", "1080p", "1440p", "2160p"]
bitrates = ["1 Mbps", "2 Mbps", "3 Mbps", "4 Mbps", "5 Mbps", 
            "6 Mbps", "7 Mbps", "8 Mbps", "9 Mbps", "10 Mbps",]
buffering_durations = [0, 1, 2, 3, 4, 5]
error_codes = [None, "err_100", "err_101", "err_102", "err_103"]

ts = int(datetime.datetime.now().timestamp() * 1000)
user_id = str(uuid.uuid4())
video_id = str(uuid.uuid4())
country = random.choice(user_countries)
resolution = random.choice(resolutions)
bitrate = random.choice(bitrates)
buffering_duration = random.choice(buffering_durations)
error_code = random.choice(error_codes)

event = {
    "ts": ts,
    "userId": user_id,
    "videoId": video_id,
    "country": country,
    "resolution": resolution,
    "bitrate": bitrate,
    "bufferingDuration": buffering_duration,
    "errorCode": error_code,
}

producer.produce(
    topic="telemetry",
    value=avro_serializer(event, SerializationContext("telemetry", MessageField.VALUE)),
)
producer.flush()