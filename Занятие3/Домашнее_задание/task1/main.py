def input_numbers():
    input_number = int(input('Введите число:')) # TODO выберите нужный цикл, чтобы получать числа с клавиатуры
    list_numbers = []

    while True:
        input_number = int(input('Введите число: '))
        if input_number < 0:
            break

        if 3 <= input_number <= 13:
            list_numbers.append(input_number)

    return list_numbers

if __name__ == "__main__":
    numbers = input_numbers()
    print(numbers)
