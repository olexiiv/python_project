import random

who = ["мій собака", "Інопланетянин", "Злий хакер", "Бетмен"]
action = ["з'їв", "викрав", "видалив", "заховав у паралельному вимірі"]
what = ["мій зошит", "інтернет кабель", "мій комп'ютер", "флешку з кодом"]

random_who = random.choice(who)
random_action = random.choice(action)
random_what = random.choice(what)

print(f"Я не зробив домашку, бо {random_who} {random_action} {random_what}.")