def bubble_sort(nums) -> list:
    sorted_nums = list(nums)
    n = len(sorted_nums)
    if n == 0: return sorted_nums
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_nums[j] > sorted_nums[j + 1]:
                sorted_nums[j], sorted_nums[j + 1] = sorted_nums[j + 1], sorted_nums[j]
    
    return sorted_nums

def insertion_sort(nums) -> list:
    sorted_nums = list(nums)
    n = len(sorted_nums)
    if n == 0: return sorted_nums

    for i in range(1, n):
        key = sorted_nums[i]
        j = i - 1
        while j >= 0 and sorted_nums[j] > key:
            sorted_nums[j + 1] = sorted_nums[j]
            j -= 1
        sorted_nums[j + 1] = key
        
    return sorted_nums

def selection_sort(nums) -> list:
    sorted_nums = list(nums)
    n = len(sorted_nums)
    if n == 0: return sorted_nums
    
    for i in range(n - 1):
        min_index = i
        
        for j in range(i + 1, n):
            if sorted_nums[j] < sorted_nums[min_index]: min_index = j
        if min_index != i:
            sorted_nums[i], sorted_nums[min_index] = sorted_nums[min_index], sorted_nums[i]
            
    return sorted_nums