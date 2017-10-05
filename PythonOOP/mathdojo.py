#OOP Bike

class MathDojo(object):

    def __init__(self):
        self.number = 0
        
        

    def add(self,add,*adds):
        total = 0
        total += result_method(add)
        for num in adds:
            total += result_method(num)
        self.number += total
        return self 

    def subtract(self,sub,*subs):
        total = 0
        total += result_method(sub)
        for num in subs:
            total = result_method(num)
        self.number -= total
        return self 
        
    def result(self):
        print self.number
        return self.number

def result_method(num):
    total = 0
    if type(num) is list or type(num) is tuple or type(num) is dict:
        for i in num:
            total += 1
    else:
        total += num
    
    return total


md = MathDojo()

md.add(2).add(2,5).subtract(3,2).result()
md.add([1],3,4).add([3,5,7,8],[2,4,3,1.25]).subtract(2,[2,3],[1.1,2,3]).result()