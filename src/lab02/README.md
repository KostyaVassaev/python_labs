# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)

## Задание 1 - `arrays.py`

### Функция `min_max`

Выполнение тест-кейсов:  
![min_max_01](../../images/lab02/arrays_01_01.png)
![min_max_02](../../images/lab02/arrays_01_02.png)

### Функция `unique_sorted`

Выполнение тест-кейсов:  
![unique_sorted_01](../../images/lab02/arrays_02_01.png)

### Функция `flatten`

Выполнение тест-кейсов:  
![flatten_01](../../images/lab02/arrays_03_01.png)
![flatten_02](../../images/lab02/arrays_03_02.png)

## Задание 2 - `matrix.py`

### Функция `isRectangular`

Используется для определения "прямоугольности" матрицы, возвращает `True/False`  

<details>
<summary>Код:</summary>
```py
def isRectangular(mat: list[list]) -> bool:
    if not mat: return True
    row_ln = len(mat[0])
    for row in mat:
        if len(row) != row_ln: return False
    return True
```
</details>

### Функция `transpose`

Выполнение тест-кейсов:  
![transpose_01](../../images/lab02/matrix_01_01.png)
![transpose_02](../../images/lab02/matrix_01_02.png)

### Функция `row_sums`

Выполнение тест-кейсов:  
![row_sums_01](../../images/lab02/matrix_02_01.png)
![row_sums_01](../../images/lab02/matrix_02_02.png)

### Функция `col_sums`

Выполнение тест-кейсов:  
![col_sums_01](../../images/lab02/arrays_03_01.png)
![col_sums_02](../../images/lab02/arrays_03_02.png)

## Задание 3 - `tuples.py`

### Функция `format_record`

Выполнение тест-кейсов:  
![format_record_01](../../images/lab02/tuples_01_01.png)