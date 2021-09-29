import random
secret_number = random.randint(1, 100)
correct_guess = False

print("Ihr Ziel ist die Geheimzahl zu erraten")
print("Die Zahl ist zwischen 1 and 100")

while not correct_guess:
    guess = int(input("Geben Sie eine Ganzzahl zwischen 1 und 100 ein! "))
    if guess < 1 or guess > 100:
        print("Fehlermeldung, Ihre Zahl liegt nicht im Suchbereich")
        print("Das Computer wird exlodieren, wenn Sie es noch Mals tun")
    elif guess > secret_number:
        print("Die Geheimzahl ist kleiner")
    elif guess < secret_number:
        print("Die Geheimzahl ist groesser")
    else:
        correct_guess = True

print("Congratulations!")
print("Du hast die Geheimzahl", secret_number, "erraten")
