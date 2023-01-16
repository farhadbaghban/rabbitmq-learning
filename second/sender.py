import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.queue_declare(queue="first", durable=True)
message = "This is Testng Message for workers"
channel.basic_publish(
    exchange="",
    routing_key="first",
    body=message,
    properties=pika.BasicProperties(delivery_mode=2),
)
print("Sent message")
channel.start_consuming()
