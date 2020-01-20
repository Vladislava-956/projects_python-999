import random


def good_function():
    digit = random.randint(10, 10000)
    digit_list = list(str(digit))
    digit_list_z = list(digit_list[::-1])
    len_digit = len(digit_list)
    digit_max = max([int(i) for i in str(digit)])
    random_number_system = random.randint(digit_max+1, 10)
    _Number_System_in_degree = []
    for z in range(len_digit):
        z = str(random_number_system ** int(z))
        _Number_System_in_degree.append(z)

    _Multiplication = []
    for y in range(len_digit):
        y = str(int(_Number_System_in_degree[y]) * int(digit_list_z[y]))
        _Multiplication.append(y)

    def plus_multiplication():
        plus = 0
        for x in _Multiplication:
            x = int(x)
            plus = plus + x
        return plus

    digit_10_number_system = plus_multiplication()

    def digit_2_number_system(digit_10_number_system, to_base=2, from_base=10):
        if isinstance(digit_10_number_system, str):
            n = int(digit_10_number_system, from_base)
        else:
            n = int(digit_10_number_system)
        alp = "0123456789"
        if n < to_base:
            return alp[n]
        else:
            return digit_2_number_system(n // to_base, to_base) + alp[n % to_base]

    lis_digit_2_number_system = list(str(digit_2_number_system(digit_10_number_system, to_base=2, from_base=10)))
    count_1_of_array = int(lis_digit_2_number_system.count('1'))
    if(count_1_of_array >= M) and (count_1_of_array <= N):
        return str(digit) + '_' + str(random_number_system)
    else:
        not_suitable_digits = []
        not_suitable_digits.append(str(digit) + '_' + str(random_number_system))
        return not_suitable_digits


count = int(input('Количество чисел: '))
M = random.randint(1, 10)
N = random.randint(M + 1, 20)
digits_all = []
for i in range(1, count + 1):
    digits_all.append(str(good_function()))
_not_suitable_digits = []
for i in digits_all:
    if (''.join([str(elem) for elem in i]).count('[')) != 1:
        _not_suitable_digits.append(''.join([str(elem) for elem in i]))
digits_all = str(digits_all)
digits_all = digits_all.strip('[')
digits_all = digits_all.strip(']')
_not_suitable_digits = str(_not_suitable_digits)
_not_suitable_digits = _not_suitable_digits.strip('[')
_not_suitable_digits = _not_suitable_digits.strip(']')
Col_vo_True_Digit = int(_not_suitable_digits.count(',')) + 1
if Col_vo_True_Digit == 1:
    Col_vo_True_Digit = 0
else:
    Col_vo_True_Digit = Col_vo_True_Digit
print('-----------------' '\n' 'Задание.')
print('Из набора ' + '%+2s ' % str(count) + 'целых чисел ' + '%+4s ' % str(digits_all))
print('записанных в разных системах счисления выбрать числа, запись которых')
print('в двоичной системе счисления имеет от' + '%+2s ' % str(M) + 'до' + '%+3s ' % str(N) + 'единиц.')
print('-----------------' '\n' 'Ответ:' '\n' 'Количество подходящих чисел' + '%+4s ' % str(Col_vo_True_Digit))
print('%+3s ' % str(_not_suitable_digits))