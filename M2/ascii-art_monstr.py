# М2.05.02 — Hook: «Монстр, якого ніколи не існувало»
# Демо для вчителя. Запускати на початку уроку, код учням НЕ показувати:
# на Рівні 7 вони напишуть ядро цього генератора самі.

import os
import random
import time

os.system("")  # вмикає кольори в терміналі Windows

COLORS = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
RESET = "\033[0m"

first = ["Зор", "Глюк", "Кракс", "Бу", "Шмяк", "Вурд", "Ксар", "Плюм"]
second = ["гар", "зіл", "тон", "бобр", "мурк", "окс", "ліп", "дзинь"]
planets = ["Kepler-22b", "Марс", "Європа", "Плутон", "Титан", "Proxima b"]

print("\n" * 30)
print("=" * 40)
print("   ГЕНЕРАТОР КОСМІЧНИХ МОНСТРІВ v1.0")
print("=" * 40)
time.sleep(1)

for number in range(1, 6):
    input(f"\n[Enter] — згенерувати монстра №{number}...")

    print("Сканую галактику", end="")
    for i in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")

    color = random.choice(COLORS)
    for row in range(6):
        half = ""
        for col in range(4):
            half += random.choice(["██", "  "])
        print("      " + color + half + half[::-1] + RESET)
        time.sleep(0.12)

    name = random.choice(first) + random.choice(second)
    print(f"\n  Ім'я:    {name}")
    print(f"  Планета: {random.choice(planets)}")
    print(f"  Сила:    {random.randint(1, 100)} / 100")

time.sleep(1)
print("\n" + "=" * 40)
print("  Різних монстрів ця програма вміє")
print(f"  намалювати: {2 ** 24:,}".replace(",", " "))
print("  Жоден із тих, кого ви бачили,")
print("  більше НІКОЛИ не з'явиться.")
print("=" * 40)