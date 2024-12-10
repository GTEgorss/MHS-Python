import threading
import time
from multiprocessing import Process

def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def measure_sync(runs):
    start_time = time.time()
    for i in range(runs):
        fibonacci(20000 + i, )
    return time.time() - start_time


def measure_threads(runs):
    threads = []
    start_time = time.time()
    for i in range(runs):
        t = threading.Thread(target=fibonacci, args=(20000 + i,))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    return time.time() - start_time


def measure_processes(runs):
    threads = []
    start_time = time.time()
    for i in range(runs):
        t = Process(target=fibonacci, args=(20000 + i,))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    return time.time() - start_time


# Example usage
if __name__ == "__main__":
    runs = 500
    sync_time = measure_sync(runs)
    thread_time = measure_threads(runs)
    process_time = measure_processes(runs)

    print(f"Synchronous execution time: {sync_time:.2f} seconds")
    print(f"Threaded execution time: {thread_time:.2f} seconds")
    print(f"Multiprocess execution time: {process_time:.2f} seconds")
