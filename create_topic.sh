KAFKA_FOLDER=/usr/lib/kafka

$KAFKA_FOLDER/bin/kafka-topics.sh \
	--create \
	--zookeeper localhost:2181 \
	--topic bitstamp.btc.transactions \
	--partitions 1 \
	--replication-factor 2 # replication-factor <= brokers number