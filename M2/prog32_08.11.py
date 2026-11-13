nik = input("Введи свій нік: ")
low = nik.lower()

vowels = 0
digits = 0
for ch in low:
  if ch in "аеиіоуяюєїaeiouy":
    vowels += 1
  if ch.isdigit():
    digits +=1

print("\n===Аналіз нікнейму===")
print(f"Нік: {nik}")
print(f"Довжина {len(nik)} символів")
print(f"Перший символ: {nik[0]}. Останній: {nik[-1]}")
print(f"Нік містить {vowels} голосних")
print(f"Нік містить {digits} цифр")
print(f"Дзеркальний нік: {nik[::-1]}")
print(f"Нік капсом: {nik.upper()}")

