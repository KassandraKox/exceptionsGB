# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
# каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.
# Важно: При выполнении метода единственное исключение, которое пользователь может увидеть - RuntimeException.

def list_div(list_a, list_b):
    if len(list_a) != len(list_b):
        print("Длины списков не равны, будет возвращён результат по минимальному значению.")
        if len(list_a) > len(list_b):
            list_a, list_b = list_b, list_a
    result = []
    for i in range(len(list_a)):
        if list_b[i] == 0:
            raise RuntimeError("В списке есть 0, на 0 делить нельзя!")
        result.append(list_a[i] // list_b[i])
    return result


a = [6, 3, 9]
b = [0, 4, 7]
print(list_div(a, b))