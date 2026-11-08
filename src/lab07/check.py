from sorting import *
from search import *

import random

def check_sorting(fn, trials=100) -> None:
    for _ in range(trials):
        length = random.randint(0, 50)
        
        nums = [random.randint(-100, 100) for _ in range(length)]
        original = list(nums)
        result = fn(nums)
        
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"

def check_search(trials=100) -> None:
    # 1. Тестирование linear_search на случайных списках против list.index
    for _ in range(trials):
        length = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(length)]
        
        if length > 0 and random.random() < 0.7: x = random.choice(nums)
        else: x = random.randint(-120, 120)
        
        try:
            expected_index = nums.index(x)
        except ValueError:
            expected_index = -1

        result = linear_search(nums, x)

        assert result == expected_index, f"linear_search вернула {result} при поиске {x} в {nums}, хотя ожидалось {expected_index}"

    # 2. Тестирование binary_search на отсортированных списках
    for _ in range(trials):
        length = random.randint(0, 50)
        nums = sorted([random.randint(-100, 100) for _ in range(length)])
        
        test_cases = []
        if length > 0:
            test_cases.append(nums[0]) # Первый (крайний) элемент
            test_cases.append(nums[-1]) # Последний (крайний) элемент
            test_cases.append(random.choice(nums)) # Случайный элемент из списка
            
        test_cases.append(-200) # Точно меньше всех элементов
        test_cases.append(200) # Точно больше всех элементов
        test_cases.append(random.randint(-120, 120)) # Произвольный элемент
        
        for x in test_cases:
            res = binary_search(nums, x)
            if res != -1:
                assert nums[res] == x, f"Функция нашла {x} в массиве {nums} по индексу {res}, хотя там находится {nums[res]}"
            else:
                assert x not in nums, f"Функция не нашла элемент {x}, хотя он есть в массиве {nums}"

def check_two_sum(trials=100) -> None:
    for _ in range(trials):
        length = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(length)]
        
        target = random.randint(-200, 200)
        
        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)
        
        if res_brute is None:
            assert res_fast is None, f"two_sum_fast вернул {res_fast}, в то время, как two_sum_brute - {res_brute}"
        else:
            assert res_fast is not None, f"two_sum_fast вернул {res_fast}, в то время, как two_sum_brute - {res_brute}"
            
            i1, j1 = res_brute
            assert i1 != j1 and nums[i1] + nums[j1] == target, f"two_sum_brute вернула {res_brute}, хотя ожидалось {target}"
            
            i2, j2 = res_fast
            assert i2 != j2 and nums[i2] + nums[j2] == target, f"two_sum_fasr вернула {res_fast}, хотя ожидалось {target}"

# ===================================================================================

if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
        check_search()
        check_two_sum()
    print("OK")