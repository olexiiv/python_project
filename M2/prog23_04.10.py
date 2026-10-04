import random

# names = ["Olexandr", "Mariya", "Іван", "Марія", "Ольга", "Андрій", "Віктор", "Олексій", "Сергій", "Юлія"] 
# print(names)
# black_names = ["Іван", "Марія"]

# for name in names:
#     if name in black_names:
#         print(f"{name}  вхід заборонено")
#     else:
#         print(f"{name}  вхід дозволено")
# print("Завершено")

# for letter in "Python":
#     print(letter)

# for number in 5:      ПОМИЛКА!!!
#     print(number)

numbers = [1, 2, 3, 2, 3, 2, 2, 3, 2, 2, 2, 56]
numbers2 = []
count_number = 0
print(numbers)
# for number in numbers:
#     print(number)
for number in numbers:
    if number != 2:
        numbers2.append(number)
    else:
        count_number += 1
print(numbers2)
print(f"Кількість чисел 2: {count_number}")