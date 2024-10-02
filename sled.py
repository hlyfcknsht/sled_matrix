import math

# Открываем файл
matrix_file = open('matrix.txt')
matrix = matrix_file.read().split()

# Преобразуем список строк в список чисел
matrix = list(map(int, matrix))

# Вычисляем шаг следа
step = int(math.sqrt(len(matrix)) + 1)

# Выводим список следа матрицы
sled = matrix[::step]
# Суммируем значения списка
print(sum(sled))

