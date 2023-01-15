import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

ch2 = connection.channel()
ch2.queue_declare("hello")


def callback(ch, method, properties, body):
    print(f"Recived {body}")


ch2.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

print("Waiting for consume , for exit press cntl+c")
ch2.start_consuming()
