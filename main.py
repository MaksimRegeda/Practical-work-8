# Задача 8.1.
prices = [100, 105, 103, 108, 110, 107, 112, 115, 111, 118]

window = 3

current_sum = 0

for i in range(window):
    current_sum += prices[i]

max_sum = current_sum
min_sum = current_sum

for i in range(window, len(prices)):
    current_sum += prices[i]
    current_sum -= prices[i - window]

    if current_sum > max_sum:
        max_sum = current_sum

    if current_sum < min_sum:
        min_sum = current_sum

print("Ціни акцій:", prices)
print("Розмір вікна:", window)
print("Максимальна сума за 3 дні:", max_sum)
print("Мінімальна сума за 3 дні:", min_sum)

print("Максимальна середня ціна:", round(max_sum / window, 2))
print("Мінімальна середня ціна:", round(min_sum / window, 2))

# Задача 8.2.
energy = [10, 15, 12, 20, 18, 14, 16, 22, 19, 13]

prefix = [0]

for value in energy:
    prefix.append(prefix[-1] + value)

def range_sum(left, right):
    return prefix[right + 1] - prefix[left]

print("Енергоспоживання:", energy)
print("Префіксні суми:", prefix)

print("Споживання за дні 1-3:",
      range_sum(0, 2), "кВт·год")

print("Споживання за дні 4-6:",
      range_sum(3, 5), "кВт·год")

print("Споживання за дні 7-10:",
      range_sum(6, 9), "кВт·год")

print("Загальне споживання:",
      prefix[-1], "кВт·год")