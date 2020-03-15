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

price = 5
price1 = 2
rating = 4.9
message = "Hallo Österreich"
is_published = True
is_not_published = False

"""print ("\nHallo " * 3)
print ("Der Preis beträgt " +str(price)+ "€.")
print ("\nBei einer Preiserhöhung könnte die Ware jedoch auch über " +str(price)+ "€ kosten.")
print ("Der Geißburger Marsch kostet nur " +str(price1)+ "€.")
raw_input()
print("Das Rating für dieses Produkt beträgt: " +str(rating)+" " +message)
#print(message)"""
print ("Wurde die letzte Publikation veröffentlicht? ")
if raw_input () == 'ja':
    print ("Condition is "+str(is_published)+ ".")
else:
    print (is_not_published)
