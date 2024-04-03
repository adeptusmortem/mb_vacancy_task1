from typing import Union
from math import sqrt

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

def polygon_area(sides: list) -> Union[int, float]:
    pass

def triangle_area(sides: list) -> Union[int, float]:
    ValidateData(sides)
    p = sum(sides)/2
    S = p
    for side in sides: S = S * (p - side)
    S = sqrt(S)
    return S