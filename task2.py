import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Задаємо кількість випадкових точок
# num_samples = 10

# Запускаємо метод Монте-Карло для обчислення π
# pi_estimate, x_inside, y_inside, x_outside, y_outside = monte_carlo_pi(num_samples)

# Виводимо результат
# print(f"Оцінка значення π за методом Монте-Карло з {num_samples} випадкових точок: {pi_estimate}")

# Візуалізація результатів
# plt.figure(figsize=(8, 8))
# plt.scatter(x_inside, y_inside, color='blue', s=1, label='Точки всередині кола')
# plt.scatter(x_outside, y_outside, color='red', s=1, label='Точки поза колом')
# circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
# plt.gca().add_patch(circle)
# plt.xlim(-1, 1)
# plt.ylim(-1, 1)
# plt.gca().set_aspect('equal', adjustable='box')
# plt.title(f"Метод Монте-Карло для оцінки π\nЧисло точок: {num_samples}\nОцінка π: {pi_estimate}")
# plt.legend()
# plt.show()
#


def monte_carlo_calc_square(num_samples):
    inside = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []
    for _ in range(num_samples):
        x = random.uniform(0, 2)
        y = random.uniform(0, 4)

        if y <= x**2:
            inside += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    estimate = 2 * 4 * inside / num_samples
    return estimate, x_inside, y_inside, x_outside, y_outside

if __name__ == "__main__":
    num_samples = 10000
    estimate, x_inside, y_inside, x_outside, y_outside = monte_carlo_calc_square(num_samples)

    # Визначення функції та межі інтегрування
    def f(x):
        return x ** 2

    a = 0  # Нижня межа
    b = 2  # Верхня межа

    spi_result, spi_error = spi.quad(f, a, b)

    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = x^2 від {str(a)} до {str(b)}. \n Кількість точок: {num_samples}, Оцінка площі: {estimate}\n Порахована площа: {spi_result}, помилка: {spi_error}')

    plt.scatter(x_inside, y_inside, color='blue', s=1, label='Точки всередині')
    plt.scatter(x_outside, y_outside, color='red', s=1, label='Точки поза')

    plt.grid()
    plt.show()
