number = int(input("Введіть число від 2 до 10: "))
print(f"Таблиця множення числа {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}") 
print(f"Таблицю на {number} побудовано!")   