#OOP Bike

class Animal(object):

    def __init__(self,name):
        self.name = name
        self.health = 100
        

    def walk(self):
        self.health -= 1
        return self 

    def run(self):
        self.health += 5
        return self

    def display_health(self):
        print "Health for the {} is {}".format(self.name, self.health)

animal1 = Animal("tiger")

animal1.walk().walk().walk().run().run().display_health()

print "________________________________________"

class Dog(Animal):  
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.health = 150
     
    def pet(self):        
        self.health += 5
        return self
        
class Dragon(Animal):   
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print "I am a Dragon "
        super(Dragon,self).display_health()



dog1 = Dog("Rover")
dog1.walk().walk().walk().run().run().pet().display_health()
print "________________________________________"

dragon1 = Dragon('Smaug')
dragon1.fly().display_health()