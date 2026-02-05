
#from dataclasses import dataclass
#@dataclass --This and the line above to not use an __init__, 

class Product:
    # three attributes with default values
    name:str = ""                                 # attribute 1
    price:float = 0.0                             # attribute 2
    discountPercent:float = 0                     # attribute 3
    quantity:int  = 0                             # attribute 4
    subTotal:float = 0.0                          # attribute 5
    priceStr:str = ""                             # attribute 6

    #'''
    # the initializer method that Python generates based on above
    def __init__(self, name="", price=0.0, discountPercent=0, quantity=0):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent
        self.quantity = quantity
    

    def getQuantitye(self):
        return self.quantity
    
    def getSubTotal(self):
        return (self.price - (self.price*self.discountPercent/100))*self.quantity
    #'''was commented out if we use dataclasses

    # a method that uses two attributes to perform a calculation
    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100
    # a method that calls another method to perform a calculation
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()
    def getPriceStr(self, country):
        priceStr = f"{self.price:.2f}"
        if country == "US": 
            priceStr += " USD"
        elif country == "DE":
            priceStr += " EUR"
        elif country == 'CA':
            priceStr += "CAD"
        return priceStr