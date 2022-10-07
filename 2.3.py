def int_to_string(value):
    single_digits = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
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


def main():
    inp = int(input('Введите число в промежутке [0, 99]: '))
    if inp > 99:
        return "Много"
    elif inp < 1:
        return None
    else:
        return int_to_string(inp)

print(main())

