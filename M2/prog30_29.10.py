pin = "1234"
attempts = 0

while True:
    user_input = input("Введіть PIN-код: ")
    if user_input == "":
      print("PIN-код не може бути порожнім. Спробуйте ще раз.")
      continue

    attempts += 1
    if user_input == pin:
        print("Доступ дозволено.")
        break
    else:
        print("Невірний PIN-код.")
        if attempts >= 3:
            print("Заблоковано після 3 невдалих спроб.")
            break