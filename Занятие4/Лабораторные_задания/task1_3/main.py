def count_even_numbers(list_numbers: list) -> int:
    list_even_numbers = [
        i
        for i in list_numbers
        if i % 2 == 0
    ]
    # TODO найти количество четных чисел в списке list_numbers

    return len(list_even_numbers)
if __name__ == "__main__":
    print(count_even_numbers(list(range(1, 25))))
