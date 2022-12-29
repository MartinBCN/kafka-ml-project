import uuid
from json import dumps
from time import sleep

import numpy as np
from kafka import KafkaProducer, KafkaAdminClient

producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    bootstrap_servers=['localhost:29094']
)

# Reset Topics
topics = ['RawData']
admin_client = KafkaAdminClient(bootstrap_servers=['localhost:29094'])
existing_topic_list = admin_client.list_topics()

for topic in topics:
    if topic in existing_topic_list:
        admin_client.delete_topics(topics=[topic])
        admin_client.create_topics([topic])
admin_client.close()

mnist_test_data = np.loadtxt('data/X_test.txt', dtype=int)
n = mnist_test_data.shape[0]

for _ in range(n):
    data = mnist_test_data[np.random.choice(n, replace=False), :]

    msg = producer.send(
        topic='RawData',
        value={
            "data": data.tolist(),
            "id": str(uuid.uuid4()),
        }
    )
    sleep(2)
