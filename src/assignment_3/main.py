import time
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
from typing import List, Tuple
import statistics


def collatz_steps(n: int) -> int:
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def process_chunk(chunk: List[int]) -> List[int]:
    return [collatz_steps(n) for n in chunk]


def parallel_collatz_processpool(numbers: List[int], num_processes: int) -> Tuple[List[int], float]:
    start_time = time.time()
    
    # Split work into chunks for better load balancing
    chunk_size = max(1, len(numbers) // (num_processes * 4))
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        chunk_results = list(executor.map(process_chunk, chunks))
    
    results = [step for chunk in chunk_results for step in chunk]
    
    end_time = time.time()
    return results, end_time - start_time


def main():
    MAX_NUMBER = 10_000_000
    num_threads = mp.cpu_count()  # Use all available CPU cores
    
    numbers = list(range(1, MAX_NUMBER + 1))
    print(f"Available CPU cores: {mp.cpu_count()}")    
    print(f"\nPROCESSPOOL PROCESSING ({num_threads} processes)")
    print("Processing all 10,000,000 numbers...")
    process_results, process_time = parallel_collatz_processpool(numbers, num_threads)
    process_avg = statistics.mean(process_results)
    print(f"Average steps: {process_avg:.2f}")
    print(f"Execution time: {process_time:.2f} seconds")
    print(f"ax steps: {max(process_results)}")
    print(f"Min steps: {min(process_results)}")


if __name__ == "__main__":
    main()