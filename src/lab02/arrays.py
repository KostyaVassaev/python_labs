def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0: raise ValueError("empty list")
    mn, mx = nums[0], nums[0]
    for n in nums:
        if n > mx: mx = n
        elif n < mn: mn = n
    return (mn, mx)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if len(nums) == 0: return nums

    nums = list(set(nums)) #убираем повторяющиеся элементы

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

#print([3, -1, 5, 5, 0], "->", min_max([3, -1, 5, 5, 0]))
#print([42], "->", min_max([42]))
#print([-5, -2, -9], "->", min_max([-5, -2, -9]))
#print([], "->", min_max([]))
#print([1.5, 2, 2.0, -3.1], "->", min_max([1.5, 2, 2.0, -3.1]))

#print([3, 1, 2, 1, 3], "->", unique_sorted([3, 1, 2, 1, 3]))
#print([], "->", unique_sorted([]))
#print([-1, -1, 0, 2, 2], "->", unique_sorted([-1, -1, 0, 2, 2]))
#print([1.0, 1, 2.5, 2.5, 0], "->", unique_sorted([1.0, 1, 2.5, 2.5, 0]))

#print([[1, 2], [3, 4]], "->", flatten([[1, 2], [3, 4]]))
#print([[1, 2], (3, 4, 5)], "->", flatten([[1, 2], (3, 4, 5)]))
#print([[1], [], [2, 3]], "->", flatten([[1], [], [2, 3]]))
#print([[1, 2], "ab"], "->", flatten([[1, 2], "ab"]))