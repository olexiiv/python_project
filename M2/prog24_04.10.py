import random

squad = ["Макс", "Соня", "Тролль228", "Артем", "Даша"]
banned = ["Тролль228"]
titles = ["Легенда", "Снайпер", "Танк", "Хілер"]
print("=== ПЕРЕКЛИЧКА ЗАГОНУ ===")
heroes = [] # сюди складемо тих, хто пройшов перевірку
count = 0 # лічильник бійців
for name in squad:
    if name in banned:
      print(f"{name} — у бані, пропускаємо.")
    else:
      title = random.choice(titles)
      print(f"{name} — звання «{title}»")
      heroes.append(name)
      count += 1
print(f"\nДо бою готові {count} бійців: {heroes}")
# Другий цикл по вже відфільтрованому списку
for hero in heroes:
    if len(hero) > 4:
      print(f"{hero}: довге ім'я, у чаті скорочуємо до {hero[0:3]}.")