class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def myfunc(self):
        print ("Mein Name ist " + self.name + " und ich bin " + str(self.age) + " Jahre alt.") #str ist elementar, um int in str zu konvertieren

p1 = Person("Chris", 28)
p1.myfunc()
