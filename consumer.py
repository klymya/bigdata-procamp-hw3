import json
import logging
import sys

import numpy as np
from kafka import KafkaConsumer


handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(handler)


KAFKA_KEY = 'nifi_produces'
KAFKA_TOPIC = 'bitstamp.btc.transactions'


def update_top10_transactions(top_transactions, upd_transactions):
    upd_transactions = np.concatenate([top_transactions, upd_transactions])
    top_idxs = np.argsort([i['data']['price'] for i in upd_transactions])[::-1][:10]
    return upd_transactions[top_idxs]


def processing_step(message_batch, top10_transactions):
    upd_transactions = [
        json.loads(msg.value.decode('utf8'))
        for batch in message_batch.values()
        for msg in batch
        if msg.key and msg.key.decode('utf8') == KAFKA_KEY
    ]
    upd_transactions = [i for i in upd_transactions if 'price' in i['data']]

    LOGGER.info(f"Received {len(upd_transactions)} transactions.")
    top10_transactions = update_top10_transactions(
        top10_transactions, upd_transactions)

    LOGGER.info(f"Top 10 transactions:\n{top10_transactions}")
    return top10_transactions


consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=['localhost:9092'],
    group_id='group-1',
    enable_auto_commit=False
)

top10_transactions = []
while True:
    input('Press enter to poll data...')

    message_batch = consumer.poll()
    top10_transactions = processing_step(message_batch, top10_transactions)
    consumer.commit()
