print('Задача 3. Число наоборот 2')


def reverse(a):
    new_numb = 0
    while a > 0:
        last_of_a = a % 10
        a //= 10
        new_numb *= 10
        new_numb += last_of_a
    return new_numb


N = int(input('Введите первое число: '))
K = int(input('Введите второе число: '))
reverse_N = reverse(N)
reverse_K = reverse(K)
summ_rev_K_N = reverse_K + reverse_N
reverse_summ_rev_K_N = reverse(summ_rev_K_N)
print('\nПервое число наоборот:', reverse_N)
print('Второе число наоборот:', reverse_K)
print('\nСумма чисел:', summ_rev_K_N)
print('Сумма наоборот:', reverse_summ_rev_K_N)
# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225