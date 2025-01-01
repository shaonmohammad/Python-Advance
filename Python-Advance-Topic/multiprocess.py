from multiprocessing import Process
import os
import time


def calculate_square(number):
    print(f"Calculating square of {number}")
    time.sleep(2)  # Simulate a delay
    print(f"Square of {number}: {number * number}")


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    processs = []
    for number in numbers:
        process = Process(target=calculate_square, args=(number,))
        processs.append(process)
        process.start()

    for p in processs:
        p.join()

    print("All calculation are done!")
