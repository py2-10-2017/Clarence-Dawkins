#OOP Bike

class Bike(object):

    def __init__(self,price, max_speed,miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Bike price is :$" + str(self.price)
        print "Max speed is : " + str(self.max_speed)
        print "Total miles: " + str(self.miles) + "mph" 

    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        print "Reversing"
        if self.miles >= 5: 
            self.miles -= 5

bike1 = Bike(49.99,85,65)
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

print "________________________________________"

bike2 = Bike(79.99,150,200)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

print "________________________________________"

bike3 = Bike(39.99,50,40)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
   