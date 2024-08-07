def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if first == 0:
        first = 1

    elif len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(int(str('00123')))
print(result)


#  При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.
