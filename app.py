import numpy as np

def spiral(matrix):
    result = []
    while matrix.size > 0:
        result.extend(matrix[0].tolist())
        matrix = matrix[1:]

        if matrix.size > 0:
            matrix = np.rot90(matrix)
    return result

array = np.random.randint(1, 101, size=(5, 5))
print("array ")
print(array)

middle_element = array[2, 2]
print("Middle Element ", middle_element)


row_mean = np.mean(array, axis=1)
print("Row Means ", row_mean)

mean = np.mean(array)
new_array = array[array > mean]
print("Elements greater than mean ", new_array)

spiralorder = spiral(array)
print("Elements in spiral order", spiralorder)
