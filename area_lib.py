###################################################################
#
# Библиотека с функциями определения площадей фигур
# 
# 1) проверяет корректность ввода данных
# 2) на данный момент библиотека содержит функции расчета площади треугольника и окружности
# 3) есть функция проверки прямоугольности треугольника
#
###################################################################

from typing import Union
from math import pi, sqrt

# Класс ошибки
class InvalidData(Exception):    
    pass

# Функция поднимает ошибку, если данные неверные
def ValidateData(sides: list) -> None: 
    # Ошибка если у многоугольника число сторон меньши 3
    if len(sides) < 3: 
        raise InvalidData('figure must have at least 3 sides')
    
    # Ошибка если в списке сторон многоугольника есть не-число
    elif False in (isinstance(side, (int, float)) for side in sides): 
        raise InvalidData('sides must be a numbers')
    
    # Ошибка если в списке сторон есть 0 или отрицательное число
    elif False in (side > 0 for side in sides):
        raise InvalidData('sides must be greater than 0')

    # Ошибка если треугольник с такими сторонами не может существовать
    elif (len(sides) == 3) and (
        False in ((sum(sides)-side) > side for side in sides)
        ):
        raise InvalidData('such triangle cannot exist')
    pass

# Функция, определяющая является ли данный треугольник пярмоугольным
def is_triangle_right(sides: list) -> bool:
    A = sides[0]
    B = sides[1]
    C = sides[2]
    return (A**2+B**2==C**2) or (A**2+C**2==B**2) or (B**2+C**2==A**2)

def triangle_area(sides: list) -> Union[int, float]:
    # Валидация данных
    ValidateData(sides)
    if len(sides) != 3: raise InvalidData('triangle must have 3 sides')

    # Проверка является ли треугольник прямоугольным
    if is_triangle_right(sides):
        A = sides[0]
        B = sides[1]
        C = sides[2]
        if (A > B) and (A > C):
            S = 0.5*B*C
        elif (B > A) and (B > C):
            S = 0.5*A*C
        else: 
            S = 0.5*A*B
        return S
    else:
        p = sum(sides)/2
        S = p
        for side in sides: S = S * (p - side)
        S = sqrt(S)
        return S
    
def cirlce_area(radius: Union[int, float]) -> Union[int, float]:
    if not isinstance(radius, (int, float)):
        raise InvalidData('radius must be a number')
    elif (radius <= 0):
        raise InvalidData('radius must be a positive number')
    else:
        return pi*radius*radius