if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_even_numbers = [
            i
            for i in list_
            if i % 2 == 0
    ] # TODO получить два списка четных и нечетных чисел

    list_odd_numbers = [
        i for i in list_
        if i % 2 == 1
    ]
    print(len(list_even_numbers))
    print(len(list_odd_numbers))

     # TODO найти длины этих списков

    ...  # TODO распечатать каких чисел больше. Учтите, что длины могу быть равны
