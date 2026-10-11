import random
players = ["Макс", "Соня", "Артем", "Даша"]
ranks = ["Золото", "Срібло", "Бронза", "Залізо"]
# 1. Реєстрація: паралельні списки через range(len(...))
print("=== КІБЕРАРЕНА: РЕЄСТРАЦІЯ ===")
for i in range(len(players)):
  print(f"#{i + 1} {players[i]} — ліга «{ranks[i]}»")
# 2. Не вистачає учасників — генеруємо ботів із числа
for i in range(1, 4):
  players.append(f"Бот_{i}")
print(f"\nДодано ботів. Учасників: {len(players)}")
print(players)
# 3. Зворотний відлік
print("\nДо старту:")
for sec in range(3, 0, -1):
  print(f"{sec}...")
print("БІЙ!")
# 4. Три раунди з випадковим переможцем
for r in range(1, 4):
  winner = random.choice(players)
  print(f"Раунд {r}: перемагає {winner}")
# 5. Рівні з босами — кожен десятий
for level in range(10, 31, 10):
  print(f"Рівень {level}: з'являється БОС")