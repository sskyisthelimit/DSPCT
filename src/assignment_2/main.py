import time, random, threading, multiprocessing

def estimate_pi(n, seed=0):
    # Monte Carlo method: generate random points in unit square and count how many fall inside unit circle
    rnd = random.Random(seed)
    inside = 0
    for _ in range(n):
        x = rnd.random()
        y = rnd.random()
        # Check if point (x,y) is inside unit circle using Pythagorean theorem
        if x*x + y*y <= 1.0:
            inside += 1
    # Pi/4 = (area of quarter circle) / (area of unit square) = inside/n
    return 4.0 * inside / n

def worker(n, seed, out_list, idx):
    out_list[idx] = estimate_pi(n, seed)

def run_threads(total_points, n_threads):
    # Distribute points evenly across threads, handle remainder
    base = total_points // n_threads
    remainder = total_points % n_threads
    counts = [0] * n_threads
    threads = []
    
    for i in range(n_threads):
        n = base + (1 if i < remainder else 0)
        t = threading.Thread(target=worker, args=(n, 1000 + i, counts, i))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    inside_total = sum(counts)
    return 4.0 * inside_total / total_points

def run_multiproc(total_points, n_procs):
    # Distribute points evenly across processes, handle remainder
    base = total_points // n_procs
    remainder = total_points % n_procs
    args = []
    
    for i in range(n_procs):
        n = base + (1 if i < remainder else 0)
        args.append((n, 2000 + i))
    
    with multiprocessing.Pool(n_procs) as pool:
        results = pool.starmap(estimate_pi, args)
    
    # Sum up pi estimates from all processes and take average
    pi_sum = sum(results)
    return pi_sum / n_procs

if __name__ == "__main__":
    N = 1_000_000
    
    t0 = time.perf_counter()
    pi = estimate_pi(N, seed=42)
    t1 = time.perf_counter()
    print(f"Single run result: pi={pi:.8f} time={t1-t0:.6f}s")
    
    for p in [1,2,4,8,16,32,64]:
        t0 = time.perf_counter()
        pi = run_multiproc(N, p)
        t1 = time.perf_counter()
        print(f"Multiprocessing result: processes={p:2d} pi={pi:.8f} time={t1-t0:.6f}s")
    
    for n in [1,2,4,8,16,32,64]:
        t0 = time.perf_counter()
        pi = run_threads(N, n)
        t1 = time.perf_counter()
        print(f"Threading result: threads={n:2d} pi={pi:.8f} time={t1-t0:.6f}s")