from json import loads

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'Results',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-1',
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    bootstrap_servers=['localhost:29094']
)

for m in consumer:
    payload = m.value
    print(payload)
