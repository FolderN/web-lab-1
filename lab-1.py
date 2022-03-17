import math


def putin():
    print("Введите x.")
    try:
        x = float(input())
    except ValueError:
        print("Неверный формат данных, завершение программы.")
        exit()
    return x


def func():
    x = putin()
    if 5 <= x < 10:
        return 1 - math.sin(x)
    elif 10 <= x < 15:
        return 1 + math.cos(x)
    elif 15 <= x < 20:
        return math.tan(x)
    elif 20 <= x < 25:
        return 1/math.tan(x)
    else:
        return 0


def main():
    print(f"Результат y(x): {func()}")


if __name__ == "__main__":
    main()
