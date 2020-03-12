print ("Willkommen\n")
print ("Zum Oeffnen des Tresors benoetigen Sie eine Kombination.\n")

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
      print ("Bitte Befehl zur Schleife eingeben: ")
      if raw_input () == 'go':
          i = 1
          while i < 6:
              i += 1
              if i == 3:
                  continue
              print i
              """print(i)
              if i == 3:
                break
                print ("\ni wurde bei 3 gestoppt.")
              i += 1"""
    else:
        raw_input ("\nHallo du Nudel.")
  else:
    raw_input ("Sie haben die falsche Zahl eingegeben. Das Programm endet hier.")
else:
  print ("Falsch. Das Programm wird nun geschlossen.")
