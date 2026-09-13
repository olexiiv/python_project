bag = ["меч", "зілля"]
print(bag)
bag.append("щит")
print(bag)
bag.insert(0, "ключ")
print(bag)
# if "ключ" in bag:
#   bag.remove("ключ")
#   print("Двері відчинено!")
# else:
#   print("Двері зачинено! Немає ключа")

# print(bag)

# item = bag.pop(1)
# print(f"Використано: {item}")
# print(bag)

# del bag[-1]
# print(bag)

# bag.clear()
# print(bag)

bag.append("зілля")
bag.insert(3, "зілля")
print(bag)
print(bag.count("зілля"))
print(bag.index("меч"))
bag2 = ["книга", "ліхтар", "зілля"]
bag.extend(bag2)
print(bag)
print(len(bag))
bag3 = bag.copy()
print(bag3)
print(bag)
bag3.remove("зілля")
print(bag3)
print(bag)