from json import loads, dumps

import joblib
import numpy as np
from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer(
    'RawData',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-1',
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    bootstrap_servers=['localhost:29094']
)

producer = KafkaProducer(
    value_serializer=lambda x: dumps(x).encode('utf-8'),
    bootstrap_servers=['localhost:29094']
)

# Load MNIST Model
filename = 'models/mnist.pkl'
clf = joblib.load(filename)

for m in consumer:
    payload = m.value
    input_data = np.array(payload['data']).reshape(1, -1)
    result = clf.predict(input_data)

    # Write Result back to Kafka
    msg = producer.send(
        topic='Results',
        value={
            "data": result.tolist()[0],
            "id": payload['id'],
        }
    )
