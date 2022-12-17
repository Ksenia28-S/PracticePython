import math

class Complex:

    def __init__(self, re, img):
        self.re = re
        self.img = img
    
    def __str__(self):
        if self.img < 0:
            return f"{self.re} - {self.img}i"
        elif self.img == 0:
            return f"{self.re}"
        else:
            return f"{self.re} + {self.img}i"
    
    def __eq__(self, other):
        return self.re == other.re and self.img == other.img
    
    def __add__(self, other):
        return Complex(self.re + other.re, self.img + other.img)
    
    def __subtract__(self, other):
        return Complex(self.re - other.re, self.img - other.img)
    
    
    def __multiply__(self, other):
        return Complex(self.re*other.re - self.img*other.img, self.re*other.img + other.re*self.img)
    
    def __modul__(self):
        return math.sqrt(self.re**2 + self.img**2)
    
    def __divide__(self, other):
        return Complex((self.re*other.re + self.img*other.img)/(other.re**2 + other.img**2), (other.re*self.img - self.re*other.img)/(other.re**2 + other.img**2))
