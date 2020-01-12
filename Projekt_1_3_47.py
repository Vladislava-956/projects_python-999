import random
def good_function():
    digit = random.randint(10, 10000)
    digit_list = list(str(digit))
    digit_list_Z = list(digit_list[::-1])
    len_digit = len(digit_list)
    def max_digit():
        assert digit_list
        m = digit_list[0]
        for i in digit_list:
            if i > m:
                m = i
        return int(m) + 1
    random_Number_System = random.randint(max_digit(), 10)

    p = []
    for i in range(len_digit):
        i = str(random_Number_System ** int(i))
        p.append(i)
    j = []
    for i in range(len_digit):
        i = str(int(p[i]) * int(digit_list_Z[i]))
        j.append(i)
    def Sum():
        Sum = 0
        for i in j:
            i = int(i)
            Sum = Sum + i
        return Sum
    digit1 = Sum()
    def dv_digit(digit1, to_base=2, from_base=10):
        if isinstance(digit1, str):
            n = int(digit1, from_base)
        else:
            n = int(digit1)
        alp = "0123456789"
        if n < to_base:
            return alp[n]
        else:
            return dv_digit(n // to_base, to_base) + alp[n % to_base]
    massiv_dv_digit = list(str(dv_digit(digit1, to_base=2, from_base=10)))
    Col_vo_Ed = int(massiv_dv_digit.count('1'))
    if(Col_vo_Ed >= M) and (Col_vo_Ed <= N):
        return str(digit) + '_' + str(random_Number_System)
    else:
        n = []
        n.append(str(digit) + '_' + str(random_Number_System))
        return n
count = int(input('Количество чисел: '))
M = random.randint(1, 10)
N = random.randint(M + 1, 20)
h = []
for i in range(1, count + 1):
    h.append(str(good_function()))
k = []
for i in h:
    if (''.join([str(elem) for elem in i]).count('[')) != 1:
        k.append(''.join([str(elem) for elem in i]))
h = str(h)
h = h.strip('[')
h = h.strip(']')
k = str(k)
k = k.strip('[')
k = k.strip(']')
Col_vo_True_Digit = int(k.count(',')) + 1
if Col_vo_True_Digit == 1:
    Col_vo_True_Digit = 0
else:
    Col_vo_True_Digit = Col_vo_True_Digit
print('Количество единиц от' + '%+2s ' % str(M) + 'до' + '%+3s ' % str(N) + '\n' '-----------------' '\n' 'Задание.' '\n' 'Из набора' + '%+2s ' % str(count) + 'целых чисел'+ '%+4s ' % str(h) + '\n'  'записанных в разных системах счисления выбрать числа, запись которых' '\n' 'в двоичной системе счисления имеет от' + '%+2s ' % str(M) + 'до' + '%+3s ' % str(N) + 'единиц.' '\n' '-----------------' '\n' 'Ответ:' '\n' 'Количество подходящих чисел' + '%+4s ' % str(Col_vo_True_Digit) + '\n' + '%+3s ' % str(k))