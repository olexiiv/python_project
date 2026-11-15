import secrets
import random

small = "abcdefghijklmnopqrstuvwxyz"
big = small.upper()
digits = "0123456789"
symbols = "!@#$%&*?"

print("=== ГЕНЕРАТОР ПАРОЛІВ PRO ===")
bag = small + big + digits + symbols

while True:
  print("Обери варіант:")
  print("1. Згенерувати пароль довільної довжини")
  print("2. Вихід")
  key = input("Введи номер варіанту: ")
  if key == "1":
    while True:
      answer = input("Задай довжину пароля (від 12 до 30): ")
      if answer.isdigit() and 12 <= int(answer) <= 30:
        length = int(answer)
        print(f"Довжина пароля: {length}")
        
        parts = [
          secrets.choice(small), # обов'язково: мала літера
          secrets.choice(big), # обов'язково: велика літера
          secrets.choice(digits), # обов'язково: цифра
          secrets.choice(symbols), # обов'язково: спецсимвол
        ]
        for i in range(length - 4): # решту місця заповнюємо будь-чим
          parts.append(secrets.choice(bag))
        random.shuffle(parts)
        password = "".join(parts)
        print(f"Згенерований пароль: {password}")
        break
      print("Потрібне число від 12 до 30. Спробуй ще раз.")
  elif key == "2":
    print("Вихід з програми.")
    break
  else:
    print("Невірний варіант. Спробуй ще раз.")
