import random

cargo = ["руда", "кисень", "кисень", "аптечка", "насіння", "скафандр", "ящик інструментів", "кава"]
print(cargo)
backup = cargo.copy()
print(backup)
print(cargo[0:3], cargo[-1])
print(cargo[3])
cargo[3] = "ПОШКОДЖЕНО!"
print(cargo)
if "кисень" in cargo:
  print(f'Кількість балонів кисню - {cargo.count("кисень")}')
else:
  print("ТРИВОГА Кисню немає!")
cargo.insert(0, "Рятувальна капсула")
print(cargo)
number_sk = cargo.index("скафандр")
cargo[1], cargo[6] = cargo[6], cargo[1]
print(cargo[0:2])
if "руда" in cargo:
  number_ruda = cargo.index("руда")
  print(f"У космос скинуто: {cargo.pop(number_ruda)}")
else: 
  print("руди немає.")
cargo.append(input("Що додати до списку?"))
print(cargo)
cargo.sort(reverse=True)
print(cargo)