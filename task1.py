import pulp

model = pulp.LpProblem("Maximize Products quantity", pulp.LpMaximize)

A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість лимонаду
B = pulp.LpVariable('B', lowBound=0, cat='Integer')  # Кількість фруктового соку

# Функція цілі (Максимізація кількості продуктів)
model += A + B, "Products quantity"

# Додавання обмежень
model += 2 * A + 1 * B <= 100   # Обмеження по воді
model += 1 * A + 0 * B <= 50  # Обмеження по цукру
model += 1 * A + 0 * B <= 30  # Обмеження по лимонному соку
model += 0 * A + 2 * B <= 40  # Обмеження по фруктовому пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти лимонаду:", A.varValue)
print("Виробляти фруктового соку:", B.varValue)
print("Максимальна кількість продуктів:", pulp.value(model.objective))