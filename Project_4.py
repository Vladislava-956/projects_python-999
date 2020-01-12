# Написать программу для нахождения суммы элементов заданной последовательности действительных чисел
# С k1 по k2 номер (k1,k2 вводятся с клавиатуры).
print('Задайте последовательность чисел с k1 по k2:')
k1 = int(input('k1 = '))
k2 = int(input('k2 = '))
sum1 = sum2 = 0
sequence = []
for i in range(k1, k2+1):
    sequence.append(i)
print('sequence =', sequence)
for i in (sequence):
    if i > 0:
        sum1 +=i
    else:
        sum2 +=i
print('Сумма положительных элементов:' + '%+3s ' % str(sum1) + '\n' 'Сумма отрицательных элементов:' + '%+3s ' % str(sum2))
