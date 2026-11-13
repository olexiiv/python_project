nik = "Olexii_123"
print(len(nik))
print(nik[4])
print(nik[-1])
print(nik[::-1])
# for letter in nik:
#   print(letter)

# print("h" in nik )
# print(nik.count("h"))
# print(nik.index("h"))
if "x" in nik:
  print(nik.index("x"))
else:
  print("Символ відсутній")

sp = [1,2,3,4,5,6,7,8,9,10]
print(sp)
sp[5] = 1000
print(sp)
print(nik)
nik = "new_text"
print(nik)
# nik = "N"+nik[1:3] 
# print(nik)
print(nik.upper())

# number = input("Введи число: ")
# if number.isdigit():
#   print("ви ввели число")
# else:
#   print("ви ввели не число")
text = list(nik)
print(text)
word = "".join(text)
print(word)