import random
secret_zeichen = random.randint(0, 255)
correct_guess = False

print("Ihr Ziel ist das Geheimzeichen zu erraten")
print("Das Zeichen kann man auch in der ASCII Tabelle finden")

while not correct_guess:
    guess = ord(input("Geben Sie in Zeichen der ASCII Tabelle ein: "))
    if guess < 0 or guess > 255:
        print("Fehlermeldung, Ihr Zeichen liegt nicht im Suchbereich")
        print("Das Computer wird exlodieren, wenn Sie es noch Mals tun")
    elif guess > secret_zeichen:
        print("Das Geheimzeichen hat ein hoeheren Wert in der ASCII Tabelle")
    elif guess < secret_zeichen:
        print("Das Geheimzeichen ein kleineren Wert in der ASCII Tabelle")
    else:
        correct_guess = True

print("Congratulations!")
print("Du hast das Geheimzeichen", chr(secret_zeichen), "erraten")
