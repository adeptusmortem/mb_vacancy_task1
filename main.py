from area_lib import triangle_area, is_triangle_right, cirlce_area, calc_area


def main() -> None:
    sides=[3,4,5]
    s = triangle_area(sides)
    r = 2
    print(f'Площадь треугольника со сторнами {sides} равна {s}')
    print(f'Треугольник со сторнами {sides} прямоугольный: {is_triangle_right(sides)}')
    print(f'Площадь окружности с радиусом {r}: {cirlce_area(r)}')
    radius = 2
    tri_sides = [3, 4, 5]
    rect_sides = [2, 2]
    print(f"""\nПлощадь фигуры с атоопределением:
Окружность с радиусом {radius} имеет площадь: {calc_area(radius)}
Триугольник со сторонами {tri_sides} имеет площадь: {calc_area(*tri_sides)}
Прямоугольник со сторонами {rect_sides} имеет площадь: {calc_area(*rect_sides)}
          """)

if __name__ == '__main__':
    main()