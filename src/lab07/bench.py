import csv
import random
import timeit
from pathlib import Path

from sorting import *
from search import *

from src.lib.outputting import table_print
from src.lab04.io_txt_csv import write_csv

random.seed(42)

def read_numbers(path):
    with open(path, encoding="utf-8") as f:
        return [int(row["value"]) for row in csv.DictReader(f)]


def bench_sorts(n):
    data = read_numbers(f"data/samples/lab07/numbers_{n}.csv")
    rows = []
    
    sorting_tasks = {
        "bubble_sort": bubble_sort,
        "insertion_sort": insertion_sort,
        "selection_sort": selection_sort,
        "built_in_sorted": sorted
    }
    
    for name, func in sorting_tasks.items():
        if n == 100000 and name in ["bubble_sort", "insertion_sort", "selection_sort"]:
            rows.append(("sort", n, name, "> 60"))
            continue
            
        # Замер времени на копии исходных данных
        t = timeit.timeit(lambda: func(data.copy()), number=1)
        rows.append(("sort", n, name, f"{t:.6f}"))
        
    return rows


def bench_search():
    rows = []
    
    n_search = 100000
    n_queries = 10000
    
    search_list = [random.randint(0, 10**6) for _ in range(n_search)]
    queries = [random.randint(0, 10**6) for _ in range(n_queries)]
    
    t_linear = timeit.timeit(lambda: [linear_search(search_list, q) for q in queries], number=1)
    rows.append(("search", n_search, "linear_search", f"{t_linear:.6f}"))
    
    t_sort_for_binary = timeit.timeit(lambda: sorted(search_list), number=1)
    rows.append(("search", n_search, "binary_search_sorting", f"{t_sort_for_binary:.6f}"))
    
    sorted_search_list = sorted(search_list)
    t_binary = timeit.timeit(lambda: [binary_search(sorted_search_list, q) for q in queries], number=1)
    rows.append(("search", n_search, "binary_search", f"{t_binary:.6f}"))
    
    two_sum_sizes = [1000, 10000]
    
    for n in two_sum_sizes:
        two_sum_data = [random.randint(0, 10**6) for _ in range(n)]
        target = random.choice(two_sum_data) + random.choice(two_sum_data)
        
        if n <= 1000:
            t_brute = timeit.timeit(lambda: two_sum_brute(two_sum_data, target), number=1)
            rows.append(("two_sum", n, "two_sum_brute", f"{t_brute:.6f}"))
        else:
            rows.append(("two_sum", n, "two_sum_brute", "> 60"))
        
        t_fast = timeit.timeit(lambda: two_sum_fast(two_sum_data, target), number=1)
        rows.append(("two_sum", n, "two_sum_fast", f"{t_fast:.6f}"))
        
    return rows


results = []
headers = ("task", "n", "impl", "seconds")

sort_sizes = [1000, 10000, 100000]
for size in sort_sizes:
    print(f"Запуск бенчмарка сортировок для n = {size}...")
    results.extend(bench_sorts(size))
    
print("Запуск бенчмарка поиска...")
results.extend(bench_search())

table_print(results, header=headers)

data_path = Path(__file__).resolve().parent.parent.parent / "data"

csv_path = Path(f"{str(data_path)}/lab07/bench.csv")
write_csv(results, csv_path, headers)
print(f"\nРезультаты успешно сохранены в {csv_path}")