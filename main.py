from area_lib import triangle_area


def main() -> None:
    sides=[3,4,5]
    s = triangle_area(sides)
    print(f'Площадь равна {s}')


if __name__ == '__main__':
    main()