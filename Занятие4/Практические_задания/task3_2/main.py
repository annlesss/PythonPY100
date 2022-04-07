if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }
    for fruit in cart:
        print(cart[fruit])  # получаем значение по ключу
    print(sum(cart.values()))   # сумма значений value это значение, а не ключ, то есть числа
    # TODO посчитать через метод values
