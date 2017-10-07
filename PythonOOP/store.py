#OOP Store

class Store(object):

    def __init__(self,location,owner):
        self.items = []                       
        self.location = location
        self.owner = owner             
        
    def add_product(self,products):        
        self.items.append(products)         

    def remove_product(self, products):
        i = 0
        while i <= (len(self.items)-1):
            if self.items[i] == products:
                del self.items[i]                
            else:
                i+=1

    def inventory_print(self):
        print "Store Location: " , self.location
        print "Store Owner: ", self.owner
        print "Current Stock: ", self.items[0:]       

def process():
    choice = raw_input("Please choose the following:  Press A - Add Product, R - Remove Product, P - Print Inventory, Q - Quit Program ")
    while choice != "Q" and choice != "q":    
        if choice == "A" or choice == "a":
            products = raw_input("Enter Product Name: ")    
            inventory.add_product(products)
        elif choice == "R" or choice == "r":
            products = raw_input("Remove Product Name: ")
            inventory.remove_product(products)
        else:  
            print ("--")*40          
            inventory.inventory_print()
            print ("--")*40
        choice = raw_input("Please choose the following:  Press A - Add Product, R - Remove Product, P - Print Inventory, Q - Quit Program ")

program = True
location = raw_input("Please enter the store location. ")
owner = raw_input("Owner(s) Name: ")
inventory = Store(location,owner)
process()