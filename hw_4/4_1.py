import time
import threading
import multiprocessing


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def run_sync(n, times=10):
    start = time.time()
    for _ in range(times):
        fib(n)
    end = time.time()
    return end - start


def run_threads(n, times=10):
    start = time.time()
    threads = []
    for _ in range(times):
        t = threading.Thread(target=fib, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    return end - start


def run_processes(n, times=10):
    start = time.time()
    processes = []
    for _ in range(times):
        p = multiprocessing.Process(target=fib, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end = time.time()
    return end - start


if __name__ == "__main__":
    n = 35
    with open('artifacts/4_1_results.txt', 'w') as f:
        sync_time = run_sync(n)
        f.write(f"Sync time: {sync_time:.4f} s\n")

        threads_time = run_threads(n)
        f.write(f"Threads time: {threads_time:.4f} s\n")

        processes_time = run_processes(n)
        f.write(f"Processes time: {processes_time:.4f} s\n")
