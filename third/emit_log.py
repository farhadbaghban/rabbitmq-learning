import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout", durable=True)
message = "this is fanout exchange testing"
channel.basic_publish(exchange="logs", routing_key="", body=message)
print("Sent message")
connection.close()
