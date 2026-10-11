count_1 = 0
for i in range(10):
    print(f"Item {i}")
    count_1 += 1

print("1 цикл завершено, кількість ітерацій:", count_1)

count_2 = 0
for i in range(5, 10):
    print(f"Item {i}")
    count_2 += 1

print("2 цикл завершено, кількість ітерацій:", count_2)

count_3 = 0
for i in range(1, 10, 3):
    print(f"Item {i}")
    count_3 += 1

print("3 цикл завершено, кількість ітерацій:", count_3)

count_4 = 0
for i in range(10, 0, -2):
    print(f"Item {i}")
    count_4 += 1

print("4 цикл завершено, кількість ітерацій:", count_4)

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
count_5 = 0
for i in range(len(list_1)):
    print(f"Item {list_1[i]}")
    count_5 += 1

print("5 цикл завершено, кількість ітерацій:", count_5) 

for i in range(10):
  print(";)"*i)