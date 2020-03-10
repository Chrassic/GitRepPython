""" geburtsjahr = input ("Gib dein Geburtsjahr an: ")
alter = 2020 - int(geburtsjahr)
print (type(alter))
print (alter) """

""" name = raw_input ("Dein Name? ")
farbe = raw_input ("Deine Lieblingsfarbe? ")
print ("Hi " + name + ", deine Lieblingsfarbe ist also " + farbe) """

"""name = raw_input ("Wie ist dein Name? ")
gewicht_pfund = input ("Ok, " + name + ". Gib nun bitte dein Gewicht in Pfund an: ")
gewicht_kilogramm = int (gewicht_pfund)* 0.45
print("Du wiegst also " + str(gewicht_kilogramm) + " Kilogramm, " + name + "; du bist ganz schoen fett")
//Das essenzielle hierbei ist 'str', weil es den string in eine zahl konvertiert"""

#STOP BEI 29.29 (Python-Video, Youtube)

print ("Willkommen\n")
print ("Zum Oeffnen des Tresors benoetigen Sie eine Kombination.\n")

x = raw_input ("Erste Zahl: ") #raw_input ist ein Muss!
x1 = raw_input ("Zweite Zahl: ")
x2 = raw_input ("Dritte Zahl: ")
if x == '2' and x1 == '5' and x2 == '9':
  print ("Richtige Kombination.\n")
  print ("Jetzt fehlt noch eine Zahl. ")
  if raw_input () == '1':
    print ("Danke.")
  else:
    raw_input ("Sie haben die falsche Zahl eingegeben. Das Programm endet hier.")
else:
  print ("Falsch.")
