print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709
def summ_of_row(precision, x):
    now = 1
    past = 0
    count = 0
    x_new = 1
    fact = 1
    while abs(now - past) > precision:
        past = now
        x_new *= x * x
        count += 1
        fact *= (count * 2 - 1) * 2 * count
        if count % 2:
            now += -1 * (x_new / fact)
        else:
            now += 1 * (x_new / fact)
    return now


precision = float(input('Введите точность: '))
x = float(input('Введите x: '))
my_summ = summ_of_row(precision, x)
print('Сумма ряда =', my_summ)
