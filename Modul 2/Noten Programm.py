note = float(input("Erste Note: "))
summe_alle_noten = note
anzahl_noten = 1

while note != 0:
    print("Zur Berechnung des Durchschnitts geben Sie 0 ein!")
    note = float(input("Weitere Note: "))
    if note != 0:
        summe_alle_noten += note
        anzahl_noten += 1
    else:
        print(summe_alle_noten / anzahl_noten)
