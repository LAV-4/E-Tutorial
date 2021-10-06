import matplotlib.pyplot as plt

dosis = int(input("Dosis? "))
frequenz = float(input("Frequenz? "))
abbaurate = float(input("Abbaurate? "))
dauer = int(input("Dauer? "))

zaehler = [0 for a in range(dauer)]
zeit = [0 for b in range(dauer)]
konzentration = [0 for c in range(dauer)]
konzentration[0] = dosis

print("Zähler | Zeit | Konzentration")
for i in range(1, len(zaehler)):
    if zaehler[i-1] == frequenz:
        zaehler[i] = 0
        zeit[i] = zeit[i-1] + 1.001
        konzentration[i] = konzentration[i-1] + dosis
    else:
        zaehler[i] = zaehler[i-1] + 1
        zeit[i] = zeit[i-1] + 1
        konzentration[i] = konzentration[i-1] * (1 - abbaurate)

    print(zaehler[i-1], "|", round(zeit[i-1], 3), "|", round(konzentration[i-1], 3))

plt.plot(konzentration)
plt.title("Medikamentenkonzentration über die Zeit")
plt.xlabel("Zeit")
plt.show()




