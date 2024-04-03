from area_lib import triangle_area, is_triangle_right, cirlce_area


def main() -> None:
    sides=[3,4,5]
    s = triangle_area(sides)
    r = 2
    print(f'Площадь равна {s}')
    print(f'Треугольник прямоугольный: {is_triangle_right(sides)}')
    print(f'Площадь треугольника с радиусом {r}: {cirlce_area(r)}')

if __name__ == '__main__':
    main()