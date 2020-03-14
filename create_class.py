class Person:
    def __init__(self, name, age, height):
      self.name = name
      self.age = age
      self.height = height
    def myfunc(self):
        print ("Mein Name ist " + self.name + " und ich bin " + str(self.age) + " Jahre alt" + " sowie " + str(self.height) + "m gross") #str ist elementar, um int in str zu konvertieren
        i = 967000/12
        print ("Der Wert von i ist ", i)
p1 = Person("Chris", 28, 1.70)
p1.myfunc()
