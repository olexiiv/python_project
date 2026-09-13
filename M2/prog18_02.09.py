import random
inventory = ["меч", "зілля", "ключ", "гриб", 100, 150] 

print(inventory)
# print(inventory[1])
# print(inventory[-1])
# print(f"Довжина списку: {len(inventory)}")
# print(inventory[0:5])
# print(inventory[2:5])
# print(inventory[4:])
inventory[0] = "Меч Дракона"
print(inventory)
inventory[-2] = inventory[-2] - 20
inventory[-1] -= 50
print(inventory)
inventory[2], inventory[3] = inventory[3], inventory[2]
print(inventory)
lucky = random.randint(0, len(inventory) - 1)
print(f"Випадковий елемент списку: {lucky}")