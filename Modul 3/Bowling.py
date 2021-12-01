spieler = int(input("Geben Sie die Anzahl Spieler "))
runden = int(input("Geben Sie die Anzahl Runden "))

tabelle = [[0 for m in range(runden)] for n in range(spieler)]

summen = [0 for x in range(spieler)]

print(tabelle)

for i in range(spieler):
    for j in range(runden):
        print("Spieler ", i + 1, ",", "Runde ", j + 1)
        tabelle[i][j] = int(input("Punkte "))
        summen[i] += tabelle[i][j]

print("Resultate ", tabelle)
print("Summen ", summen)
