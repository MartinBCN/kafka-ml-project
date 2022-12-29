from json import dumps
from time import sleep

from kafka import KafkaProducer

producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    bootstrap_servers=['localhost:29094'])

for _ in range(60):
    msg = producer.send("test", value={"hello": "producer"})
    sleep(2)
