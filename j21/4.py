# رسم لوزی در پایتون

# تعداد ردیف های پایین و بالای لوزی
half_rows = 5
row_index = 0

# حلقه اول برای چاپ بالای لوزی
for i in range(1, half_rows + 1):
    # چاپ فضاهای خالی هر ردیف
    for j in range(1, (half_rows - i) + 1):
        print(end=" ")
    # چاپ ستاره ها
    while row_index != (2 * i - 1):
        print("*", end="")
        row_index = row_index + 1
    row_index = 0
    print()

# تعداد فضاهای خالی در شروع نیمه پایینی
empy_spaces = 2
row_index = 1

# حلقه دوم برای چاپ پایین لوزی
for i in range(1, half_rows):
    # چاپ فضاهای خالی
    for j in range(1, empy_spaces):
        print(end=" ")
    empy_spaces = empy_spaces + 1
    # چاپ ستاره های هر ردیف
    while row_index <= (2 * (half_rows - i) - 1):
        print("*", end="")
        row_index = row_index + 1
    row_index = 1
    print()
