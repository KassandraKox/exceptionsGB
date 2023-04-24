# Посчитать сумму содержимого массива

def sum2d(arr):
    summ = 0
    for i in range(len(arr)):
        for j in range(5):
            try:
                summ += int(arr[i][j])
            except ValueError:
                continue
            except IndexError:
                break
    return summ


array = [["1", "1", "0"], ["1", "1", "1"], ["1", "1", "6"]]
print(sum2d(array))