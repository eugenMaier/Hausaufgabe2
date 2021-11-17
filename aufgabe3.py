"Name: Eugen Maier"
"Klasse: ETS2021"
"Datum: 17.11.2021"

import math                                         #math funktionen werden hinzugefügt
import time                                         #time funktionen werden hinzugefügt


x = int(input("Bitte die erste Zahl eingeben  "))   #eingabe von der ersten zahl
y = int(input("Bitte die zweite Zahl eingeben  "))  #eingabe von der zweiten zahl




for i in range (x,y+1):                             #for schleife mit den oben vorgegebenen Bereich +1 um den ganzen gewolten Bereich abzudeckne
    if i > 1:                                       #alle Primzahlen sind größer als 1
        for z in range (2,int(i)):                  #Läuft alle Zhalen von 2 bis i durch
            if i % z == 0:                          #wenn i in modulu kein Rest hat ist es Keine Primzahl
             break                                  #wenn i keine Primzahl brich die Schleife ab
        else:
            print(i)                                #wenn i Reste hat Gib i aus





        