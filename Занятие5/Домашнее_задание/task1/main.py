def print_table(size: int = 9):
    matrix = [[] for _ in range(size)]  # формируем список пустых списков

    for i in range(size):  # цикл по индексам строк
        for j in range(size):  # цикл по индексам столбцов
            row = matrix[i]
            row.append((i+1)*(j+1))

    for row_index in range(size):
        for col_index in range(size):
            print(f"{matrix[row_index][col_index]:2}", end=" ")
        print()


if __name__ == "__main__":
    print_table()
