farben = ["Pik", "Karo", "Herz", "Kreuz"]
kartenWerte = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 20]
symbol = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
anzahl_karten = int(input("Wie viele Karten? "))
summe = 0

for i in range(anzahl_karten):
    print("Pik=1 | Karo=2 | Herz=3 | Kreuz=4")
    farben_auswahl = int(input("Welche Farbe? "))
    print("2=2 | 3=3 | ... | 10=10 | J=11 | Q=12 | K=13 | A=14")
    symbol_auswahl = int(input("Welches Symbol? "))
    print(farben[farben_auswahl-1], symbol[symbol_auswahl-2])
    summe += kartenWerte[symbol_auswahl-2]


print("Summe der Kartenwere:", summe)

'''for i in range(len(farben)):
    for j in range(len(symbol)):
        print(farben[i], symbol[j])'''
