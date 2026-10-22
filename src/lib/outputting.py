def table_print(rows: list[list | tuple], header: tuple[str, ...] | None = None) -> None:
    if not rows and not header: return

    num_columns = len(header) if header else (len(rows[0]) if rows else 0)
    if num_columns == 0: return

    str_rows = [[str(item) for item in row] for row in rows]
    str_header = [str(h) for h in header] if header else []

    col_widths = []
    for col_idx in range(num_columns):
        header_len = len(str_header[col_idx]) if str_header else 0
        max_row_len = max((len(row[col_idx]) for row in str_rows), default=0)
        col_widths.append(max(header_len, max_row_len))
    
    row_template = " | ".join(f"{{:<{w}}}" for w in col_widths)

    if str_header:
        print(row_template.format(*str_header))
        total_width = sum(col_widths) + 3 * (num_columns - 1)
        print("-" * total_width)

    for row in str_rows:
        print(row_template.format(*row))
