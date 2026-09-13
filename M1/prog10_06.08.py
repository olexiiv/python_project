piece = int(input("скільки шматків піци ти можеш з'їсти? "))
piece_pizza = int(input("скільки шматків піци в коробці? "))
if piece < 0:
    print("Ти що, збираєшся випльовувати піцу? ")
else:
    if piece > piece_pizza:
        print("Замовляємо ще одну піцу!")
    if piece <= piece_pizza:
        print("Смачного!")
