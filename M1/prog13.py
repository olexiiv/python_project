weather_rating = int(input("Введи оцінку температури від 0 до 35."))
if weather_rating >= 35:
    print("Ну і пекло! Краще не виходити на вулицю!")
elif weather_rating >= 20:
    print("Погода супер, можна гуляти")
elif weather_rating >= 10:
    print("Прохолодно, треба вдягнути куртку!")
else:
    print("Жах! Це якись північний полюс!")