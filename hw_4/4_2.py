import math
import time
import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing

logging.basicConfig(filename='artifacts/4_2_log.txt', level=logging.INFO, format='%(asctime)s %(message)s')


def partial_integrate(f, a, b, n_iter):
    step = (b - a) / n_iter
    acc = 0
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10_000_000):
    interval_length = (b - a) / n_jobs
    tasks = []
    for i in range(n_jobs):
        sub_a = a + i * interval_length
        sub_b = sub_a + interval_length
        sub_n_iter = n_iter // n_jobs
        tasks.append((f, sub_a, sub_b, sub_n_iter))
    return tasks


def measure_time(executor_class, f, a, b, n_jobs_list, n_iter=10_000_00):
    results = []
    for n_jobs in n_jobs_list:
        tasks = integrate(f, a, b, n_jobs=n_jobs, n_iter=n_iter)
        start = time.time()
        with executor_class(max_workers=n_jobs) as executor:
            futures = []
            for idx, (func, sub_a, sub_b, sub_n_iter) in enumerate(tasks):
                logging.info(f"Starting task {idx + 1}/{n_jobs} with interval [{sub_a}, {sub_b}]")
                futures.append(executor.submit(partial_integrate, func, sub_a, sub_b, sub_n_iter))
            total = sum(f.result() for f in futures)
        end = time.time()
        elapsed = end - start
        results.append((n_jobs, elapsed, total))
    return results


if __name__ == "__main__":
    cpu_num = multiprocessing.cpu_count()
    n_jobs_list = range(1, cpu_num * 2 + 1)
    thread_results = measure_time(ThreadPoolExecutor, math.cos, 0, math.pi / 2, n_jobs_list)
    process_results = measure_time(ProcessPoolExecutor, math.cos, 0, math.pi / 2, n_jobs_list)

    with open('artifacts/4_2_timings.txt', 'w') as f:
        f.write("Threads:\n")
        for n_jobs, elapsed, total in thread_results:
            f.write(f"n_jobs={n_jobs}, time={elapsed:.4f}s, result={total}\n")

        f.write("\nProcesses:\n")
        for n_jobs, elapsed, total in process_results:
            f.write(f"n_jobs={n_jobs}, time={elapsed:.4f}s, result={total}\n")
