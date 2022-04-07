def task(n: int, m: int) -> list: # TODO записать функцию с аннотацией типов
    list_ = [
        i ** 2
        for i in range(n, m + 1)
    ]    # TODO с помощью list comprehension найти квадраты целых чисел
    return list_

if __name__ == "__main__":
    number_n = 10
    number_m = 20

    print(task(number_n, number_m))
