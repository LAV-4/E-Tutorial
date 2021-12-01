import random

ToDoListe = []

ToDoFach = ["Chemie", "Informatik", "Mathematik", "Geographie"]
ToDoHandlung = ["repetieren", "Aufgabe", "Doku"]

while True:
    print("")
    print("Was willst du?")
    print("N=Neues ToDo | L=ToDo Löschen | P=ToDoListe |")
    char = input("Beliebige andere Taste=Beenden ")

    if char == "N":
        neuesToDo = str(random.choice(ToDoFach) + " " + random.choice(ToDoHandlung))
        ToDoListe.append(neuesToDo)
        print(neuesToDo)
    elif char == "L":
        print(ToDoListe)
        loeschen_index = int(input("Welches löschen? "))
        ToDoListe.pop(loeschen_index)
        print("Anzahl ToDos", len(ToDoListe))

    elif char == "P":
        print(ToDoListe)

    else:
        print("Meine ToDos:", ToDoListe)
        print("Anzahl ToDos", len(ToDoListe))
        break
print("Viel Erfolg bei der Arbeit")
