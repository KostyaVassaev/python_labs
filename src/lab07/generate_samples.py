import csv
import random
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
data_path = project_root / "data"

def generate_test_samples():
    random.seed(42)
    
    sizes = [1000, 10000, 100000]
    
    output_dir = Path(f"{str(data_path)}/samples/lab07")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for n in sizes:
        file_path = output_dir / f"numbers_{n}.csv"
        
        random_numbers = [random.randint(0, 10**6) for _ in range(n)]
        
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["value"])
            for num in random_numbers:
                writer.writerow([num])
                
        print(f"Файл успешно создан: {file_path} ({n} строк)")

generate_test_samples()