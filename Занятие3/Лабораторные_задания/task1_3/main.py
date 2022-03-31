def get_list_number_divisors(number):
    result = [] #TODO найти список делителей числа number
    for d in list(range(1, number + 1)):
        if number % d == 0:
            result.append(d)
    return result


if __name__ == "__main__":
    print(get_list_number_divisors(2 ** 16))
