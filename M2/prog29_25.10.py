# Бейдж
# nick = input("Введи свій нік: ")
# width = len(nick) + 4
# print("+" + "-" * width + "+")
# print("|" + " " * width + "|")
# print("|  " + nick + "  |")
# print("|" + " " * width + "|")
# print("+" + "-" * width + "+")

#Ялинка
# h = 15
# for i in range(1, h + 1):
#     print(" " * (h - i) + "#" * (2*i-1))

#Шахова дошка
# size = 9
# for i in range(size):
#     if i % 2 == 0:
#         print("██  " * (size // 2))
#     else:
#         print("  ██" * (size // 2))

#Персонаж
# hero = [
# "   ##### ",
# "  #     # ",
# " #  O O  #",
# "#   ---   #",
# " ######## ",
# "   # # # ",
# " ## ## ## ",
# ]
# for row in hero:
#   print(row)

#Ялинка
import random

h = 7
decor = ["*", "*", "*", "*", "o", "@", "+", "*"]

for i in range(1, h + 1):
  row = ""
  for j in range(2*i-1):
    row += random.choice(decor)
  print(" " * (h - i) + row)
