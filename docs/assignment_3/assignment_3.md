# Analysis of Parallel Collatz Iteration

## Methodology

A **CPU-bound** Collatz iteration function was applied across an integer range. The work was split into multiple chunks that were processed **concurrently** by separate worker processes. Results were then aggregated to compute summary statistics and execution time.

---

## Key Results

* **Average Iteration Count**: The average number of steps for the evaluated range.
* **Observed Extremes**: The minimum and maximum iteration counts found.
* **Total Execution Time**: The measured wall-clock time on the test machine.

---

## Conclusions & Implications

Parallel process-based execution successfully **reduced the wall-clock time** for this heavy computation. However, it also introduces *memory and inter-process communication overhead*, which can be a limiting factor when applied to very large input ranges.