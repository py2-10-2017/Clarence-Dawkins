#OOP Product

class product(object):

    def __init__(self,price,item_name,weight,brand,cost):
        self.price = price                  
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        self.display_info()

    def sell(self):
        self.status = "Sold"
        self.display_info()

    def add_tax(self, tax):
        self.price = self.price + tax
        self.display_info()
        

    def item_return(self,reason): 
        self.reason = reason           
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "open item":
            self.status = "used"
            self.price = self.price - (self.price * 0.20)
        else:
            self.status = "like new"
        self.display_info()  
    
    def display_info(self):
        print "Price :$" + str(self.price)
        print "Item :" + self.item_name
        print "Weight: " + str(self.weight)
        print "Brand: " + self.brand
        print "Cost :$ "  + str(self.cost)
        print "Status :" + self.status
    
product1 = product(4.99,"Fidget Spinner",0.5,"Macco",2.99)

print "________________________________________"

product1.sell()
print "________________________________________"
product1.add_tax(0.5)
print "________________________________________"
product1.item_return("like new")



