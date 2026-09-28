# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)

## Задание 1 - `arrays.py`

### Функция `min_max`

**Код:**  
```py
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0: raise ValueError("empty list")
    mn, mx = nums[0], nums[0]
    for n in nums:
        if n > mx: mx = n
        elif n < mn: mn = n
    return (mn, mx)
```

Выполнение тест-кейсов:  
![min_max_01](../../images/lab02/arrays_01_01.png)
![min_max_02](../../images/lab02/arrays_01_02.png)

### Функция `unique_sorted`

**Код:**  
```py
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if len(nums) == 0: return nums

    nums = list(set(nums)) #убираем повторяющиеся элементы

    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
```

Выполнение тест-кейсов:  
![unique_sorted_01](../../images/lab02/arrays_02_01.png)

### Функция `flatten`

**Код:**  
```py
def flatten(mat: list[list | tuple]) -> list:
    res = []
    for row in mat:
        if type(row) != list and type(row) != tuple:
            raise TypeError("list and tuple only")
        res += list(row)
    return res
```

Выполнение тест-кейсов:  
![flatten_01](../../images/lab02/arrays_03_01.png)
![flatten_02](../../images/lab02/arrays_03_02.png)

## Задание 2 - `matrix.py`

### Функция `isRectangular`

Используется для определения "прямоугольности" матрицы, возвращает `True/False`  

**Код:**  
```py
def isRectangular(mat: list[list]) -> bool:
    if not mat: return True
    row_ln = len(mat[0])
    for row in mat:
        if len(row) != row_ln: return False
    return True
```

### Функция `transpose`

**Код:**  
```py
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not isRectangular(mat): raise ValueError("only rectangular matrix")
    if not mat or not mat[0]: return []

    rows = len(mat)
    cols = len(mat[0])
    t_mat = [[None for i in range(rows)] for j in range(cols)]

    for i in range(rows):
        for j in range(cols):
            t_mat[j][i] = mat[i][j]
    return t_mat
```

Выполнение тест-кейсов:  
![transpose_01](../../images/lab02/matrix_01_01.png)
![transpose_02](../../images/lab02/matrix_01_02.png)

### Функция `row_sums`

**Код:**  
```py
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not isRectangular(mat): raise ValueError("only rectangular matrix")

    res = []
    for row in mat:
        res.append(sum(row))
    return res
```

Выполнение тест-кейсов:  
![row_sums_01](../../images/lab02/matrix_02_01.png)
![row_sums_01](../../images/lab02/matrix_02_02.png)

### Функция `col_sums`

**Код:**  
```py
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not isRectangular(mat): raise ValueError("only rectangular matrix")

    rows = len(mat)
    cols = len(mat[0])
    res = [0] * cols

    for i in range(rows):
        for j in range(cols):
            res[j] += mat[i][j]
    return res
```

Выполнение тест-кейсов:  
![col_sums_01](../../images/lab02/arrays_03_01.png)
![col_sums_02](../../images/lab02/arrays_03_02.png)

## Задание 3 - `tuples.py`

### Функция `format_record`

**Код:**  
```py
def format_record(rec: tuple[str, str, float]) -> str:
    if len(list(rec)) != 3: raise TypeError("not valid length of incoming tuple")

    fio, group, gpa = rec[0].split(), rec[1], rec[2]
    if not (2 <= len(fio) <= 3): raise ValueError("not valid fio")
    if not (0.0 <= gpa <= 5.0): raise ValueError("not valid gpa")

    formated_fio = f"{fio[0][0].upper() + fio[0][1:]} "
    for i in range(1, len(fio)):
        formated_fio += f"{fio[i][0].upper()}."

    return f"{formated_fio}, гр. {group.upper()}, GPA {gpa:.2f}"
```

Выполнение тест-кейсов:  
![format_record_01](../../images/lab02/tuples_01_01.png)