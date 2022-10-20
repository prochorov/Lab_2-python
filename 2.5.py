def int_to_string(value):
    single_digits = ["ноль", "одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    two_digit1 = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
                  "семьнадцать", "восемнадцать", "девятнадцать"]
    two_digit2 = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семдесят", "восемьдесят",
                  "девяносто"]

    if value < 10:
        return single_digits[value]
    elif value < 20:
        return two_digit1[value - 10]

    tens = int(value / 10)
    reminder = value % 10
    result = two_digit2[tens - 2]
    if reminder != 0:
        result += " " + int_to_string(reminder)
    return result


inp = int(input('Введите число в промежутке [0, 99]: '))

if inp < 1:
    print("Число должно быть один или больше")
    exit(0)

v1 = "сидела"
v2 = "сидело"
V1 = "синица"
V2 = "синицы"
V3 = "синиц"
if inp % 10 == 1 and inp != 11:
    s1 = v1
    s2 = V1
elif inp % 10 == 2 or inp % 10 == 3 or inp % 10 == 4 and inp != 12 and inp != 13 and inp != 14:
    s1 = v2
    s2 = V2
else:
    s1 = v2
    s2 = V3
if inp > 99:
    s3 = "много"
else:
    s3 = int_to_string(inp)
s = f'На дереве {s1} {s3} {s2}.'
print(s)
