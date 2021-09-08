personen_im_kurs = 13
anwesend_heute = int(input("Wie viele Personen sind heute anwesend? "))

if anwesend_heute < 0 or anwesend_heute > 13:
    print("Geben Sie Zahlen im Bereich von 0 bis 13 an.")
elif personen_im_kurs > anwesend_heute:
    print("Anzahl Personen, die fehlen:", personen_im_kurs - anwesend_heute)
else:
    print("Alle Personen sind anwesend. Yay!")
