"Name: Eugen Maier"
"Klasse: ETS2021"
"Datum: 17.11.2021"

import math                                         #math funktionen werden hinzugefügt
import time                                         #time funktionen werden hinzugefügt



while True:                                         #Loop wird erstellt
    print("\n\n")                                   #2 Leerzeichen werden ausgegeben
    x=input("Bitte die Erste Zahl eingeben  ")      #Man wird aufgefordert die erste Zahl einzugeben
    print("\n\n")                                   #2 Leerzeichen werden ausgegeben
    y=input("Bitte die zweite Zahl eingeben  ")     #Man wird aufgeforder die zweite Zahl auszugeben

    x=int(x)                                        #Macht aus der Eingabe eine Zahl

    y=int(y)

    for i in range (x,y):                           #Guckt alle Zhalen von x bis y durch

        if i % 9 == 0:                              #Schaut ob die Zahlen durch 9 Teilbar sind
            print(i)                                #Gibt alle Zahlen aus die durch 9 Teilbar sind
    time.sleep(10)                                  #wartet 10 s

