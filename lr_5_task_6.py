# -*- coding: utf-8 -*-
"""Lr_5_task_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HDCCFPYtFJtZybDue4BOvSo0OJwwvsuw
"""

import numpy as np
import matplotlib.pyplot as plt
!pip install neurolab
import neurolab as nl

# Генерація тренувальних даних
min_val = -10
max_val = 10
num_points = 100
x = np.linspace(min_val, max_val, num_points)
y = 3 * np.square(x) + 7

# Створення даних та міток
data = x.reshape(num_points, 1)
labels = y.reshape(num_points, 1)

# Побудова графіка вхідних даних
plt.figure()
plt.scatter(data, labels)
plt.xlabel('Размерность 1')
plt.ylabel('Размерность 2')
plt.title('Входные данные')
plt.show()

# Визначення багатошарової нейронної мережі
nn = nl.net.newff([[min_val, max_val]], [5, 5, 5, 5, 1])

# Задання градієнтного спуску як навчального алгоритму
nn.trainf = nl.train.train_gd

# Тренування нейронної мережі
error_progress = nn.train(data, labels, epochs=1000, show=100, goal=0.01)

# Виконання нейронної мережі на тренувальних даних
output = nn.sim(data)
y_pred = output.reshape(num_points)

# Побудова графіка помилки навчання
plt.figure()
plt.plot(error_progress)
plt.xlabel('Количество эпох')
plt.ylabel('Ошибка обучения')
plt.title('Изменение ошибки обучения')
plt.show()

# Побудова графіка результатів
x_dense = np.linspace(min_val, max_val, num_points * 2)
y_dense_pred = nn.sim(x_dense.reshape(x_dense.size, 1)).reshape(x_dense.size)

plt.figure()
plt.plot(x_dense, y_dense_pred, '-', x, y, 'x', x, y_pred, 'p')
plt.title('Фактические и прогнозные значения')
plt.show()