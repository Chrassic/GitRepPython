#Trump-Fake-Twitter-Bot
import random
#print (random.randint(0, 4)) #generiere Zufallszahl

tweet1 = ["Merkel,", "Obama,", "The WHO,", "China,", "Harry Potter,", "Chris E."]
tweet2 = ["responsible for Corona,", "on the way down,", "looking like a fool,"]
tweet3 = ["got destroyed by my talent.", "was not smarter than me.", "debauched.", "rigged the election."]
tweet4 = ["This is an official Playtech standpoint.", "So true.", "I will go home now.", "Apologies."]
tweet5 = ["Sincerely, Trumpy-Cat", "Sincerely, your Donald without Duck"]

tweets = [tweet1, tweet2, tweet3, tweet4, tweet5] #tweets = "Überliste"
twitter_sentence = []

for tweet in tweets:
    r = random.randint(0, len(tweet)-1)
    twitter_sentence.append(tweet[r])
    #print(tweet[r])
print (" ".join(twitter_sentence)+".") #join = transformiere die Liste in einen Satz.
