def put_in():
    print("Введите целое число n. (2 <= n <= 9).")
    try:
        n = int(input())
    except ValueError:
        print("Ошибка ввода.")
        exit()
    if n > 9 or n < 2:
        print("Число не входит в промежуток.")
        exit()
    return n


def table():
    n = put_in()
    print("Таблица умножения:")
    for i in range(1, 10):
        print(i, "x", n, "=", i*n)


def main():
    table()


if __name__ == '__main__':
    main()