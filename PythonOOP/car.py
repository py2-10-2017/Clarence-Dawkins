#OOP Bike

class Car(object):

    def __init__(self,price, speed,fuel, mileage):
        self.price = price
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.10            
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()

    def display_all(self):
        print "Price :$" + str(self.price)
        print "Speed :" + str(self.speed) + " mph"
        print "Fuel: " + self.fuel
        print "Mileage: " + str(self.mileage) + " mpg"
        print "Tax: "  + str(self.tax)

    
car1 = Car(2000,35,"Full",15)

print "________________________________________"

car2 = Car(2000,5,"Not Full",105)


print "________________________________________"

car3 = Car(2000,5,"Not Full",95)


print "________________________________________"

car4 = Car(2000,25,"Kind of Full",95)


print "________________________________________"

car5 = Car(2000,45,"Empty",25)


print "________________________________________"

car6 = Car(200000000,35,"Empty",15)


