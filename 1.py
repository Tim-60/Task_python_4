import math
squares = [(x+1) ** 2 for x in range(10)]
print(squares)

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
dict = {days[i]: i+1 for i in range(7)}
print(dict)

tags_of_libs = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"] 
low_tags_of_libs = set([tags_of_libs[i].lower() for i in range(len(tags_of_libs))])
print(low_tags_of_libs)

numbers = [1, 3, 4, 87, 98, 15, 7, 4] 
even_numbers = [numbers[i] for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(even_numbers)

dict_of_factorials = {keys+1: math.factorial(keys+1) for keys in range(5)}
print(dict_of_factorials)