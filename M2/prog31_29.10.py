import random

number = random.randint(1, 100)
max_attempts = 7
attempts = 0
won = False

print("Вгадай число від 1 до 100. У тебе є 7 спроб.")
while attempts < max_attempts:
  answer = input("Введи число: ")
  if answer == "":
    print("Введіть число, будь ласка.")
    continue

  answer = int(answer)
  attempts += 1

  if answer == number:
    print("Вітаю! Ти вгадав число.")
    won = True
    break
  elif answer < number:
    print("Число більше.")
  else:
    print("Число менше.")

if not won:
  print(f"Ти не вгадав. Це було число {number}.")

#print(number)  # This line is for debugging purposes; remove it in production