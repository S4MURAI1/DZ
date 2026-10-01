import math

def square(side):
    area = side * side
    return math.ceil(area)

side_value = float(input("Введите сторону квадрата: "))
result = square(side_value)
print(f"Площадь квадрата: {result}")
