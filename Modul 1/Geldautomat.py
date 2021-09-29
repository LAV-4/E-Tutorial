'''import time     # imported library for the function time.sleep
print("WILLKOMMEN BEI DER BANK IHRES VERTRAUENS")
print("****************************************")
abheben_str = input("Wie viel möchten Sie abheben? ")
abheben_int = int(abheben_str)
print("Eingegebener Geldbetrag: " + abheben_str + " Fr.")

print("Bitte warten...")
time.sleep(1)

print("Sie haben erhalten: ")

anzahl_100 = abheben_int // 100     # Ergibt wie viele 100er zu abheben sind
print("100er " + str(anzahl_100))   # Druckt wie wie viele 100er zu abheben sind
abheben_int = abheben_int - anzahl_100 * 100    # Ergibt wie viel Geld noch abzuheben ist

anzahl_50 = abheben_int // 50
print("50er " + str(anzahl_50))
abheben_int = abheben_int - anzahl_50 * 50

anzahl_20 = abheben_int // 20
print("20er " + str(anzahl_20))
abheben_int = abheben_int - anzahl_20 * 20

anzahl_10 = abheben_int // 10
print("10er " + str(anzahl_10))
abheben_int = abheben_int - anzahl_10 * 10

rest = abheben_int
print("Rest: " + str(rest))
'''

print("WILLOMMEN BEI DER BANK IHRES VERTRAUENS")
print("****************************************")

Betrag= int(input("Wie viel möchten Sie abheben?"))

print("Eingegebener Geldbetrag:")
print(Betrag, "CHF")

print("Bite warten...")




hunderter= Betrag // 100
print("100er:", hunderter)


fünfziger = Betrag % 100// 50
print("50er:", fünfziger)


zwanziger=Betrag % 100%50//20
print("20er:",zwanziger)


zehner= Betrag % 100% 50% 20 // 10
print("10er:", zehner)

rest=Betrag% 100% 50% 20% 10

print("rest:", rest)
