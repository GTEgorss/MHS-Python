import logging
import os
import threading
import time

import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

logging.basicConfig(
        filename='artifacts/integrate.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
logger = logging.getLogger()


def partial_integral(f, start, end, num_iter):
    logger.info(f"-->Thread id: {threading.get_ident()}. From {start:.2f} to {end:.2f}")
    acc = 0
    partial_step = (end - start) / num_iter
    for i in range(num_iter):
        acc += f(start + i * partial_step) * partial_step

    logger.info(f"<--Thread id: {threading.get_ident()}")
    return acc

def integrate_executor(executor, type, f, a, b, *, n_jobs=1, n_iter=10000000):
    logger.critical(f"Begin {type}: {n_jobs} jobs")
    start = time.time()

    step = (b - a) / n_jobs
    tasks = [(a + i * step, a + (i + 1) * step, n_iter // n_jobs) for i in range(n_jobs)]

    results = []
    futures = [executor.submit(partial_integral, f, start, end, num_iter) for start, end, num_iter in tasks]
    for future in futures:
        result = future.result()
        results.append(result)

    result_sum = sum(results)
    duration = time.time() - start
    logger.critical(f"End {type}. {n_jobs} jobs. {duration:.2f} seconds.")
    return result_sum

def integrate_threads(f, a, b, *, n_jobs=1, n_iter=10000000):
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        result = integrate_executor(executor, "threads", f, a, b, n_jobs=n_jobs, n_iter=n_iter)

    return result

def integrate_processes(f, a, b, *, n_jobs=1, n_iter=10000000):
    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        result = integrate_executor(executor, "processors", f, a, b, n_jobs=n_jobs, n_iter=n_iter)

    return result

if __name__ == "__main__":
    for i in range(1, 2 * os.cpu_count() + 1):
        result_threads = integrate_threads(math.cos, 0, math.pi / 2, n_jobs=i)
        result_processes = integrate_processes(math.cos, 0, math.pi / 2, n_jobs=i)