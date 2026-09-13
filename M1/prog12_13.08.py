meme_rating = int(input("введи оцінку мему від 1 до 10."))
if meme_rating == 10:
    print("Це розрив! Відправляю всім друзям! ")
elif meme_rating >= 7:
    print("Норм мем, піде ")  
elif meme_rating >= 4:
    print("Трохи крінж, але посміхнувся ")
else:
    print("Повний крінж, видаляй інтернет ")