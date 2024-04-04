###################################################################
#
# Модуль тестов функций area_lib.py
# Список тестов:
# 1) правильность расчета площади фигуры для функций cirlce_area, triangle_area
# 2) правильность определения прямоугольного треугольника для функции is_triangle_right
# 3) проверка поднятия ошибки InvalidData при неправильном значении аргумента 
#    (0, отрицательоне, нечисло, много/мало аргументов, неадеквтность аргументов) 
#    для вышеуказаных функций
#
###################################################################


from unittest import TestCase, main
from area_lib import triangle_area, is_triangle_right, cirlce_area, InvalidData
from math import pi

class TestArea(TestCase):

    def test_cirlce_area(self):
        self.assertEqual(cirlce_area(3), pi*3**2)
        self.assertEqual(cirlce_area(111), pi*111**2)
        self.assertEqual(cirlce_area(2.1), pi*2.1**2)
        self.assertEqual(cirlce_area(pi), pi*pi**2)

    def test_circle_zero(self):
        with self.assertRaises(InvalidData) as e:
            cirlce_area(0)
        self.assertEqual('radius must be a positive number and greater than 0', e.exception.args[0])

    def test_circle_negative(self):
        with self.assertRaises(InvalidData) as e:
            cirlce_area(-1)
        self.assertEqual('radius must be a positive number and greater than 0', e.exception.args[0])

    def test_circle_non_numeric(self):
        with self.assertRaises(InvalidData) as e:
            cirlce_area('hello world')
        self.assertEqual('radius must be a number', e.exception.args[0])
            

    def test_triangle_area(self):
        self.assertEqual(round(triangle_area([1,1,1]), 2), 0.43)
        self.assertEqual(round(triangle_area([3,4,5]), 2), 6)
        self.assertEqual(round(triangle_area([147.1,224.5,99.7]), 2), 5624.13)
    
    def test_triangle_invalid_size(self):
        with self.assertRaises(InvalidData) as e:
            triangle_area([999,1,2])
        self.assertEqual('such triangle cannot exist', e.exception.args[0])
    
    def test_triangle_zero(self):
        with self.assertRaises(InvalidData) as e:
            triangle_area([0,1,2])
        self.assertEqual('sides must be greater than 0', e.exception.args[0])
    
    def test_triangle_negative(self):
        with self.assertRaises(InvalidData) as e:
            triangle_area([-1,1,2])
        self.assertEqual('sides must be greater than 0', e.exception.args[0])
    
    def test_triangle_not_enough_arg(self):
        with self.assertRaises(InvalidData) as e:
            triangle_area([1,1])
        self.assertEqual('triangle must have 3 sides', e.exception.args[0])
    
    def test_triangle_too_much_arg(self):
        with self.assertRaises(InvalidData) as e:
            triangle_area([1,1,1,1,1])
        self.assertEqual('triangle must have 3 sides', e.exception.args[0])
    
    def test_triangle_non_numeric(self):
        with self.assertRaises(InvalidData) as e:
            triangle_area([1,1,'1'])
        self.assertEqual('sides must be a numbers', e.exception.args[0])


    def test_is_triangle_right(self):
        self.assertEqual(is_triangle_right([3,4,5]), True)
        self.assertEqual(is_triangle_right([72,97,65]), True)
        self.assertEqual(is_triangle_right([666,666,666]), False)

if __name__ == '__main__':
    main()