"Name: Eugen Maier"
"Klasse: ETS2021"
"Datum: 17.11.2021"

import math                                         #math funktionen werden hinzugefügt
import time                                         #time funktionen werden hinzugefügt

kapital = input("Bitte das Darlehen eingeben  ")    #kapital eingeben
zinssatz = input("Bitte den Zinssatz eingeben  ")   #zinssatz eingeben
zeitraum = input("Bitte den Zeitramen angeben  ")   #zeitraum eingeben

kapital = int ( kapital )                           #wird zu einer Zhal umgewandelt
zinssatz = int ( zinssatz )
zeitraum = int ( zeitraum )

zinsen = kapital*(1+zinssatz/100)**zeitraum         #Jahreszinssatz wird berechnet

zinsen=(round(zinsen,2))                            #Jahreszinssatz wird nach 2 stellen nach dem Komma gerundet

print(zinsen)                                       #Ausgabe Zinsen


monatsraten = (zinsen)/(zeitraum*12)                #Monatsraten werden berechnet

monatsraten=(round(monatsraten,2))                  #Monatsraten werden gerundet

print("Ihre Monatsraten betragen", monatsraten, "Euro") #Monatsraten werden ausgegeben
