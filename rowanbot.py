#Rowan-Bot
import random

rowan1 = ["Alan,", "Adam,", "Ellie,", "Byron,"]
rowan2 = ["from an official Playtech standpoint:", "I am telling you:", "you are asking for a payrise?", "hang on..."]
rowan3 = ["That's a no", "This is outrageous", "Go on and stock the shelves", "This is a Playtech-special which means Playtech gets a special treatment", "I am waiting for my thirty thousand Dollar bonus muahahaha"]

rowans = [rowan1, rowan2, rowan3]
rowan_sentence = [] #Liste rowan_sentence

for rowan in rowans:
    r = random.randint(0, len(rowan)-1)
    rowan_sentence.append(rowan[r]) #Füge in die Liste rowan_sentence eine der rowan-Listen mit einem r ein, also einer Zufallszahl
print (" ".join(rowan_sentence)+"!") #Konvertiere die Liste rowan_sentence in einen Satz mit .join
