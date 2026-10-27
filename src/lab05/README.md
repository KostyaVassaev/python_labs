# JSON и конвертации (JSON↔CSV, CSV→XLSX)

**JSON (JavaScript Object Notation)** — текстовый формат для обмена структурированными данными.
Хранит объекты и списки, используется для сериализации и API.

**CSV (Comma-Separated Values)** — табличный текстовый формат, где значения разделены запятыми или `;`.

## Задание A — JSON ↔ CSV

### Тест-кейсы

**Тест 1**

`people.json` -> `people.csv`

Запуск и результат:

![run](../../images/lab05/json_to_csv_people.png)

![result](../../images/lab05/OUT_people_csv.png)

**Тест 2**

`people.csv` -> `people.json`

Запуск и результат:

![run](../../images/lab05/csv_to_json_people.png)

![result](../../images/lab05/OUT_people_json.png)

**Тест 3**

Пустой csv-файл ![empty.csv](../../data/samples/empty.csv)

Запуск и результат:

![empty_csv](../../images/lab05/empty_csv.png)

**Тест 4**

Пустой json-файл ![empty.json](../../data/samples/empty.json)

Запуск и результат:

![empty_csv](../../images/lab05/empty_json.png)

**Тест 5**

csv-файл только с заголовком  ![only_header.csv](../../data/samples/only_header.csv)

Запуск и результат:

![empty_csv](../../images/lab05/only_header_csv.png)

**Тест 6**

Не существующий csv-файл

Запуск и результат:

![empty_csv](../../images/lab05/csv_does_not_exist.png)

**Тест 7**

`phones.json` -> `csv.json`

Запуск 

## Задание B — CSV → XLSX

Для работы с `XLSX` используется `openpyxl`

### Работа с файлом XLSX

**Подготовка книги и сохранение:**
```py
wb = Workbook()
ws = wb.active
ws.title = "Sheet1"

# ...

wb.save(xlsx_path)
```

`active` открывает первую страницу (таблицу) из файла

### Размер колонок в файле XLSX

Для изменения размера колонок используется `get_column_letter` из `openpyxl.utils`

```py
from openpyxl.utils import get_column_letter
```

**Логика изменения размера колонок:**
```py
for col in ws.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws.column_dimensions[col_letter].width = max(max_len + 1, 8)
```

`col_letter = get_column_letter(col[0].column)` - получает букву колонки

`ws.column_dimensions[col_letter].width = max(max_len + 1, 8)` - устанавливает ширину: максимум из длины текста (+ запас) или 8 - минимальный размер по ТЗ

### Тест-кейсы

**Тест 1**

`cities.csv` -> `cities.xlsx`

Запуск и результат:

![run](../../images/lab05/csv_to_xlsx_cities.png)

![result](../../images/lab05/OUT_cities_xlsx.png)

**Тест 2**

`exmple1.csv` -> `example1.xlsx`

Исходный файл:

![example1.csv](../../data/samples/example1.csv)

Запуск:

![example1_csv_to_xlsx](../../images/lab05/csv_to_xlsx_example1.png)

Результат:

![result1.xlsx](../../data/out/result1.xlsx)

![OUT_result1.xlsx](../../images/lab05/OUT_result1_xlsx.png)