MAX_ARRAY_LENGTH = 10


def get_element(arr):
    if len(arr) > MAX_ARRAY_LENGTH:
        return -1
    else:
        return len(arr)


array = [1, 3, 4, 5, 9, 10]
print(get_element(array))