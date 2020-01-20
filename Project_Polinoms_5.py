# Написать программу для сложения двух полиномов разной степени.
# Коэффициенты полиномов­слагаемых получать случайным образом.
import random


def  input_list(count_elements):
    X = []
    for i in range(count_elements):
        x = random.randint(1, 9)
        X.append(x)
    return X

col_simvolovF = random.randint(3, 6)
print('col_simvolovF: ', col_simvolovF)
f = input_list(col_simvolovF)
print('Заданы случайные коэффициенты полинома F')
for i in range(col_simvolovF):
    print('F[' , i,'] = ' , f[i], sep=' ', end='    ')
print()
col_simvolovG = random.randint(3, 6)
print('col_simvolovG: ', col_simvolovG)
g = input_list(col_simvolovG)
#print('G', g)
print('Заданы случайные коэффициенты полинома G')
for i in range(col_simvolovG):
    print('G[' , i,'] = ' , g[i], sep=' ', end='   ')
h = []
min_len = col_simvolovF
if col_simvolovG < min_len:
    min_len = col_simvolovG
for i in range(min_len):
    x = f[i] + g[i]
    h.append(x)
if col_simvolovF  > col_simvolovG:  
    for i in range(min_len, col_simvolovF):
        h.append(f[i])
else:
    for i in range(min_len, col_simvolovG):
        h.append(g[i])
print('\nСумма полиномов(h) = ', h)
print('-----------------')
print('%+6s ' % str(h[0]) , end='+')
print('%+6sx ' % str(h[1]) , end='+')
for i in range(2, len(h)-1):
    if  h[i] != 0:
        res = str(h[i]) +'x^' + str(i)
        print('%+6s ' % res, end='+')
print('%+6sx^%d' % (str(h[len(h)-1]), len(h)-1))
