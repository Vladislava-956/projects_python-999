#Написать программу для вычисления значения полинома и его производной.
import operator
print('Введите коэффициенты полинома через пробел:')
k = list(map(int, input('Elements: ').split( )))
h = []
colvo_simv = len(k)
for i in range(colvo_simv):
    h.append(i)
u = list(map(operator.mul, k, h))
u = u[1:]
print('Заданные элементы полинома: ')
print('%+6s ' % str(k[0]) , end='+')
for i in range(0 , len(k)-1):
    if h[i] != 0:
        res = str(k[i]) + 'x^' + str(i)
        print('%+5s ' % res, end='+')
print('Производные от коэф.: ', u)
print('%+2sx^%d' % (str(k[len(h) - 1]), len(k) - 1))
print('Выведенные производные от элементов полинома',u)
print('Сумма выведенных производных = ', sum(u))

