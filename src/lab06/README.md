# CLI‑утилиты с argparse

Для реализации использовался модуль argspace - стандартный инструмент Python для парсинга аргументов командной строки.

```py
import argparse
```

## CLI обработчик текста

### Демонстрация

**Тест 1**

![A1_cat](../../images/lab06/A1_cat.png)

**Тест 2**

![A2_stats](../../images/lab06/A2_stats.png)

### Обработка ошибок

**Кейс 1: файл не существует**

![ERR_cat_no_file](../../images/lab06/ERROR_cat_no_such_file.png)

![ERR_stats_no_file](../../images/lab06/ERROR_stats_no_such_file.png)

### Справка

![H_text_total](../../images/lab06/H_cli_text_total.png)

![H_text_cat](../../images/lab06/H_cli_text_cat.png)

![H_text_stats](../../images/lab06/H_cli_text_stats.png)

## CLI-конвертер

### Демонстрация

**Тест 1**

Вызов:

![B1_terminal](../../images/lab06/B1_json2csv_terminal.png)

Исходный JSON-файл:
```json
[
  {
    "name": "Alice",
    "age": 22,
    "city": "SPB"
  },
  {
    "name": "Bob",
    "age": 25,
    "city": "Moscow"
  },
  {
    "name": "Carlos",
    "age": 30,
    "city": "Kazan"
  },
  {
    "name": "Dana",
    "age": 21,
    "city": "SPB"
  },
  {
    "name": "Andrey",
    "age": 27,
    "city": "Novosibirsk"
  }
]
```

Итог:

![B1_result](../../images/lab06/B1_json2csv_result.png)

### Обработка ошибок

**Кейс 1: файл не существует**

Вызовы и ошибки:

![ERR_json2csv_no_file](../../images/lab06/ERROR_json2csv_no_such_JSON_file.png)

![ERR_csv2json_no_file](../../images/lab06/ERROR_csv2json_no_such_CSV_file.png)

![ERR_csv2xlsx_no_file](../../images/lab06/ERROR_csv2xlsx_no_such_CSV_file.png)

**Кейс 2: неверные аргументы**

Вызовы и ошибки:

### Справка

![H_json2csv](../../images/lab06/H_json2csv.png)

![H_csv2json](../../images/lab06/H_csv2json.png)

![H_csv2xlsx](../../images/lab06/H_csv2xlsx.png)