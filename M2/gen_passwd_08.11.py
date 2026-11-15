import secrets

small = "abcdefghijklmnopqrstuvwxyz"
big = small.upper()
digits = "0123456789"
symbols = "!@#$%&*?"

bag = small+big+digits+symbols
# print(bag)
passwd = ""
print("\n===Генерація паролів===")
count_char = int(input("Скільки символів в паролі? "))
for char in range(count_char):
  passwd += secrets.choice(bag)
print(passwd)
