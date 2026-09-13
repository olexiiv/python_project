import random

print("Кидаємо кубик...")
number = random.randint(-10, 2)
print(f"Випало число: {number}")
print(type(number))

items = ["яблуко", "банан", "вишня", "груша", "апельсин"]
print(f"Випадковий фрукт: {random.choice(items)}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print(f"Перемішаний список чисел: {numbers}")