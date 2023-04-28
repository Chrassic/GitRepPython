#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import sys
# Encoding der Standardausgabe und des Dateisystems herausfinden
stdout_encoding = sys.stdout.encoding or sys.getfilesystemencoding()
fs_encoding = sys.getfilesystemencoding()
# Kompletten Kommandozeilenaufruf übernehmen und nach Unicode umwandeln
cmd_original = " ".join(sys.argv)
cmd_unicode = cmd_original.decode(fs_encoding)
# String verändern und wieder an die Kommandozeile übergeben
cmd_unicode += u" (öäü)"
#print cmd_unicode.encode(stdout_encoding)

print ("Willkommen\n")
print ("Zum Öffnen des Tresors benötigen Sie eine Kombination.\n")

x = raw_input ("Erste Zahl: ") #raw_input ist ein Muss!
x1 = raw_input ("Zweite Zahl: ")
x2 = raw_input ("Dritte Zahl: ")
if x == '2' and x1 == '5' and x2 == '9': #Alle drei muessen richtig sein!
  print ("Richtige Kombination.\n")
  print ("Bitte geben Sie die finale Zahl ein: ")
  if raw_input () == '1':
    print ("Danke. Das Programm wird fortgesetzt.\n")
    name = raw_input ("Wie lautet Ihr Name? ")
    farbe = raw_input ("Wie ist Ihre Lieblingsfarbe? ")
    print ("Hi " + name + ", Ihre Lieblingsfarbe ist also " + farbe)
    if name == 'Chris' or name == 'chris':
      print ("\nHallo, Chef.\n")
      print ("Sie sehen jetzt das aktuelle Datum sowie Zeit.\n")
      import showtime
      raw_input () #fuer Tastendruck
      print ("Fibonacci-Folge bis 10:")
      import test
      raw_input () #fuer Tastendruck
      print ("\nBitte Befehl zur Schleife eingeben: ")
      if raw_input () == 'go':
          i = 0
          while i < 5:
              i += 1
              print ("Die Schleife wurde " + str(i) + " mal ausgeführt.")
              #if i == 4:
                #  continue
                #print ("Die Schleife wurde " + str(i) + " mal ausgefuehrt.")
              #else:
                  #print ("Die Schleife wurde " + str(i) + " mal ausgefuehrt.")
              """print(i)
              if i == 3:
                break
                print ("\ni wurde bei 3 gestoppt.")
              i += 1"""
      else:
        raw_input ("\nHallo du Nudel.")
        print ("\nDie Eingabe war falsch. Das Programm wird beendet.")
  else:
    raw_input ("Sie haben die falsche Zahl eingegeben. Das Programm endet hier.")
else:
  print ("Falsch. Das Programm wird nun abgebrochen.")
