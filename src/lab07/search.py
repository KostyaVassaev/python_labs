def linear_search(nums, x) -> int:
    for i in range(len(nums)):
        if nums[i] == x: return i
    return -1

def binary_search(sorted_nums, x) -> int:
    l, r = 0, len(sorted_nums) - 1

    while l <= r:
        mid = (l + r) // 2
        a = sorted_nums[mid]
        if a == x:
            return mid
        if a > x:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def two_sum_fast(nums, target) -> tuple[int, int] | None:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None