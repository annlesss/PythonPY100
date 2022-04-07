def more_than_mean(list_numbers: list):
    average_ = sum(list_numbers) / len(list_numbers) # TODO найти среднее арифметическое списка

    more_than_mean = [
            num
            for num in list_numbers
            if num > average_
        ] # TODO с помощью list comprehension вернуть новый список
    return more_than_mean

if __name__ == "__main__":
    print(more_than_mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
