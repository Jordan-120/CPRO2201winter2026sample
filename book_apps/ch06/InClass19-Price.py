from dataclasses import dataclass

# a class with three attributes and two methods
@dataclass                           # dataclass decorator
class Product:
    name:str                         # attribute 1
    price:float                      # attribute 2
    discountPercent:int              # attribute 3
    quantity:int                     #Att4

    #Sub total
    def getSubtotal(self):
        return self.price * self.quantity

    # a method that uses two attributes
    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    # a method that calls another method
    def getDiscountPrice(self):
        return self.price - (self.getSubtotal() - self.getDiscountAmount())
    

# create two product objects
product1 = Product("Stanley 13 Ounce Wood Hammer", 12.99, 62, 10)
product2 = Product('National Hardware 3/4" Wire Nails', 5.06, 0, 10)

# print data for product1 to console
print("PRODUCT DATA")
print(f"Name:             {product1.name}")
print(f"Price:            {product1.price:.2f}")
print(f"Quantity:         {product1.quantity}")
print(f"Discount percent: {product1.discountPercent:d}%")
print(f"Discount amount:  {product1.getDiscountAmount():.2f}")
print(f"Discount price:   {product1.getDiscountPrice():.2f}")
