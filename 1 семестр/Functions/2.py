import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib.widgets import Slider, RadioButtons, Button


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



# Создание графика функции
graph = plt.subplot(1,1,1)
graph.plot(x, y, label="y = f(x)", color="red")    # График функции
line_tangent, = plt.plot(x_tangent, y_tangent, label="tangent", color="blue")    # Касательная в т. x0
line_normal, = plt.plot(x_normal, y_normal, label="normal", color="yellow")    # Нормаль в т. x0
point_x0, = plt.plot(x0, f(x0), 'o', label="x0", color='green')   # Обозначение т. x0
plt.grid()
plt.title("Функция f(x)")


# Функция для обновления графика
def update_graph():
    global slider_x0
    global line_tangent
    global line_normal
    global graph
    global point_x0
    global radiobuttons_color

    # Изменение цвета графика
    colors = {'Красный': 'r', 'Синий': 'b', 'Зеленый': 'g'}
    style = colors[radiobuttons_color.value_selected]
    graph.plot(x, y, style)

    # Просчитывание новых значений для касательной и нормали
    x0 = slider_x0.val
    f_pr_x0 = np.interp(x0, x, proizvodnaya)
    x_tangent = np.linspace(x0 - 1, x0 + 1, 1000)
    y_tangent = tangent(x_tangent, x0, f_pr_x0)
    x_normal = np.linspace(x0 - 1, x0 + 1, 1000)
    y_normal = normal(x_normal, x0, f_pr_x0)

    # Обновление данных для их отображения
    line_normal.set_data(x_normal, y_normal)
    line_tangent.set_data(x_tangent, y_tangent)
    point_x0.set_data([x0], [f(x0)])


    plt.draw()

def onCheckClicked(label):
    update_graph()


def onChangeGraph(value):
    update_graph()


def onRadioButton(label):
    update_graph()


def resetSlider(value):
    slider_x0.set_val(x0)
    update_graph()


def tangentVisible(bool):
    global tangent_visible
    tangent_visible = not tangent_visible
    line_tangent.set_visible(tangent_visible)
    update_graph()


def normalVisible(bool):
    global normal_visible
    normal_visible = not normal_visible
    line_normal.set_visible(normal_visible)
    update_graph()

# Создание слайдера
plt.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.55) # Отступ от графика
axes_slider_x0 = plt.axes([0.05, 0.35, 0.85, 0.04])
slider_x0 = Slider(axes_slider_x0, label="x0", valmin=0, valmax=5, valinit=x0, valstep=0.1)

slider_x0.on_changed(onChangeGraph)

# Создание кнопки сброса слайдера в начальное положение
axes_reset_button = plt.axes([0.35, 0.15, 0.2, 0.1])
reset_button = Button(axes_reset_button, 'Начальное пол.')
reset_button.on_clicked(resetSlider)


# Создание переключателя цвета графика
axes_radiobuttons = pylab.axes([0.05, 0.05, 0.2, 0.2])
radiobuttons_color = RadioButtons(axes_radiobuttons,
                                  ['Красный', 'Синий', 'Зеленый'])
radiobuttons_color.on_clicked(onRadioButton)

# Создание кнопки видимости касательной
tangent_visible = True
axes_tangent_visible = plt.axes([0.6, 0.15, 0.2, 0.1])
tangent_visible_button = Button(axes_tangent_visible, 'Касательная')
tangent_visible_button.on_clicked(tangentVisible)

# Создание кнопки видимости нормали
normal_visible = True
axes_normal_visible = plt.axes([0.6, 0.05, 0.2, 0.1])
normal_visible_button = Button(axes_normal_visible, 'Нормаль')
normal_visible_button.on_clicked(normalVisible)


plt.show()
