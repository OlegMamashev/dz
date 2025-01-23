import numpy as np
import matplotlib.pyplot as plt


# Задавание уравнения функции
def f(i):
    return np.sin(i) * np.cos(i**2 + 5)


def tangent(i, x0, f_pr_x0):
    f_x0 = f(x0)
    return f_x0 + f_pr_x0 * (i - x0)

def normal(i, x0, f_pr_x0):
    f_x0 = f(x0)
    return f_x0 - (1/f_pr_x0) * (i - x0)


x = np.linspace(0, 5, 1000)
y = f(x)

y_min = np.min(y)   # Нахождение максимальных и минимальных значений функции
y_max = np.max(y)
x_min = x[np.argmin(y)] # Соответствующие значения x для этих точек
x_max = x[np.argmax(y)]

# Нахождение производной функции
proizvodnaya = np.gradient(y, x)

# Нахождение второй производной функции
vtoraya_proizvodnaya = np.gradient(proizvodnaya, x)

# Вызов функции нахождения касательной и нормали
x0 = float(input("Введите т. x0: "))
f_pr_x0 = np.interp(x0, x, proizvodnaya)
x_tangent = np.linspace(x0-1, x0+1, 1000)
y_tangent = tangent(x_tangent, x0, f_pr_x0)
x_normal = np.linspace(x0-1, x0+1, 1000)
y_normal = normal(x_normal, x0, f_pr_x0)

plt.figure(figsize=(10, 7))

# Создание графика функции
plt.subplot(2, 2, 1)
plt.plot(x, y, label="y = f(x)")    # График функции
plt.plot(x_tangent, y_tangent, label="tangent", color="red")    # Касательная в т. x0
plt.plot(x_normal, y_normal, label="normal", color="yellow")    # Нормаль в т. x0
plt.scatter(x0, f(x0), color='green')   # Обозначение т. x0
plt.scatter(x_min, y_min, color='red')
plt.scatter(x_max, y_max, color='red')
plt.grid()
plt.title("Функция f(x)")

# Создание графика производной
plt.subplot(2, 2, 2)
plt.plot(x, proizvodnaya, label="y = f'(x)")
plt.grid()
plt.title("Произовднаая f(x)")

# Создание графика второй производной
plt.subplot(2, 2, 3)
plt.plot(x, vtoraya_proizvodnaya, label="y = f''(x)")
plt.grid()
plt.title("Вторая производная f(x)")

plt.show()
