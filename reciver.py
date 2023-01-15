import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

    ch2 = connection.channel()
    ch2.queue_declare("hello")

    def callback(ch, method, properties, body):
        print(f"Recived {body}")

    ch2.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    print("Waiting for consume , for exit press cntl+c")
    ch2.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
