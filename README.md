# bigdata-procamp-hw3
Bigdata procamp homework #3

## Requirements
- nifi
- kafka
- python3

## Instruction
1. Launch multiple kafka brokers(2 or more).
2. Launch nifi.
3. Create a kafka topic: `bash create_topic.sh`. Configure the path to kafka and bootstrap-server's address in the script before if needed.
4. Launch kafka producer: upload the `kafka_producer.xml` template to the hifi and start processors.
5. Install requirements: `pip install -r requirements.txt`.
6. Launch kafka consumer: `python consumer.py`.Configure bootstrap-server's address in the script before if needed.