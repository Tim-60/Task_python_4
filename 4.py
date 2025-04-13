def decorator(function):
    def wrapper(*args, **kwargs):
        print(f"Функция {function.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        return function(*args, **kwargs)
    return wrapper

@decorator
def calculate_area(length: float | int, width: float | int) -> float | int:
    return f'Площадь прямоугольника: {length * width}'

a = input('Длина: ')
if a.lstrip(' ').find('-') == 0:
        raise ValueError('Длина должна быть положительной!')
elif a.isdigit():
         a = int(a)
elif a.replace('.','', 1).isdigit():
         a = float(a)

b = input('Ширина: ')
if b.lstrip(' ').find('-') == 0:
        raise ValueError('Ширина должна быть положительной!')
elif b.isdigit():
         b = int(b)
elif b.replace('.','', 1).isdigit():
         b = float(b)

if isinstance(a, str) or isinstance(b, str):
        raise ValueError("Введены НЕ числа!")

print(calculate_area(a, b))