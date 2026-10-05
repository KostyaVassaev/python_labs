def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0: raise ValueError("empty list")
    mn, mx = nums[0], nums[0]
    for n in nums:
        if n > mx: mx = n
        elif n < mn: mn = n
    return (mn, mx)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if len(nums) == 0: return nums

    nums = list(set(nums))

    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

def flatten(mat: list[list | tuple]) -> list:
    res = []
    for row in mat:
        if type(row) != list and type(row) != tuple:
            raise TypeError("list and tuple only")
        res += list(row)
    return res