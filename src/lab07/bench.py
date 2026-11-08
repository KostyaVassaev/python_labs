import timeit
import csv
import random

from sorting import *
from search import *

random.seed(42)

results = []

# ==========================================
# 1. ТЕСТ СОРТИРОВОК
# ==========================================
print("Запуск бенчмарка сортировок...")
sorting_tasks = {
    "bubble_sort": bubble_sort,
    "insertion_sort": insertion_sort,
    "selection_sort": selection_sort,
    "built_in_sorted": sorted
}

sort_sizes = [1000, 10000, 100000]

for n in sort_sizes:
    data = [random.randint(0, 10**6) for _ in range(n)]
    
    for name, func in sorting_tasks.items():
        if n == 100000 and name != "built_in_sorted":
            continue

        def test_sort(): return func(data)
        
        seconds = timeit.timeit(test_sort, number=1)
        results.append({
            "task": "sorting",
            "n": n,
            "impl": name,
            "seconds": f"{seconds:.6f}"
        })

# ==========================================
# 2. ТЕСТ ПОИСКА
# ==========================================
print("Запуск бенчмарка поиска...")
n_search = 100000
n_queries = 10000

search_list = [random.randint(0, 10**6) for _ in range(n_search)]
queries = [random.randint(0, 10**6) for _ in range(n_queries)]

def test_linear():
    for q in queries:
        linear_search(search_list, q)
        
seconds_linear = timeit.timeit(test_linear, number=1)
results.append({
    "task": "search",
    "n": n_search,
    "impl": "linear_search",
    "seconds": f"{seconds_linear:.6f}"
})

search_list = sorted(search_list)

def test_binary():
    for q in queries:
        binary_search(search_list, q)
        
seconds_binary = timeit.timeit(test_binary, number=1)
results.append({
    "task": "search",
    "n": n_search,
    "impl": "binary_search",
    "seconds": f"{seconds_binary:.6f}"
})

# ==========================================
# 3. ТЕСТ TWO SUM
# ==========================================
print("Запуск бенчмарка Two Sum...")
two_sum_sizes = [1000, 10000]

for n in two_sum_sizes:
    two_sum_data = [random.randint(0, 10**6) for _ in range(n)]
    target = random.randint(0, 2 * 10**6)
    
    if n <= 1000:
        seconds_brute = timeit.timeit(lambda: two_sum_brute(two_sum_data, target), number=1)
        results.append({
            "task": "two_sum",
            "n": n,
            "impl": "two_sum_brute",
            "seconds": f"{seconds_brute:.6f}"
        })
    
    seconds_fast = timeit.timeit(lambda: two_sum_fast(two_sum_data, target), number=1)
    results.append({
        "task": "two_sum",
        "n": n,
        "impl": "two_sum_fast",
        "seconds": f"{seconds_fast:.6f}"
    })

import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
src_path = project_root / "src"
data_path = project_root / "data"
sys.path.append(str(src_path))
sys.path.append(str(data_path))

from lib.outputting import table_print
from lab04.io_txt_csv import write_csv

table_print(results, header=("task", "n", "impl", "seconds"))

norm_res = []
for row in results:
    norm_res.append([row.get(k, "") for k in results[0].keys()])
csv_path = Path(f"{data_path}/lab07/bench.csv")
write_csv(norm_res, csv_path, ("task", "n", "impl", "seconds"))