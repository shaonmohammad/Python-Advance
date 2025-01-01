import threading
from threading import Thread, Lock
from queue import Queue
import time

database_value = 0


def increase(lock):
    global database_value

    with lock:
        local_value = database_value
        local_value += 1
        time.sleep(0.1)
        database_value = local_value


if __name__ == "__main__":
    print('start value', database_value)
    lock = Lock()
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)


def send_messages():
    while True:
        message = input("You: ")
        print(f"Sending: {message}")


def receive_messages():
    while True:
        print("New message received!")
        time.sleep(3)  # Simulate receiving messages every 3 seconds


# Create threads for sending and receiving
thread1 = threading.Thread(target=send_messages)
thread2 = threading.Thread(target=receive_messages)

thread1.start()
thread2.start()
