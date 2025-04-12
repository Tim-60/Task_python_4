import math
def simple_number(number: int):
    for i in range(2, number):
        flag = True
        for j in range(2, round(math.sqrt(i))+1):
            if i % j == 0:
                flag = False
        if flag == True:
            yield i

num = input('Введите целое, положительное число (поиск производится до введенного числа включительно): ')
if num.isdigit():
    num = int(num)
else: 
    raise ValueError('Неверный ввод! Введите целое, положительное число!')
for a in simple_number(num+1):
    print(a)