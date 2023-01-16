import sys, os, pika, time


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="first", durable=True)

    def callback(ch, method, properties, body):
        print(f"Recieved {body}")
        time.sleep(9)
        print("Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="first", on_message_callback=callback)
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupt")
        try:
            exit(0)
        except SystemExit:
            os._exit(0)
