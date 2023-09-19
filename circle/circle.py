import math

class Circle():
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError ("El radio debe ser mayor a Cero")
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def set_radius (self, radius):
        if radius <= 0:
            raise ValueError ("El radio debe ser mayor a cero")
        self.radius = radius

    def get_area(self):
        return (math.pi * self.radius ** 2)
    
    def get_perimeter(self):
        return (2 * math.pi * self.radius)
    
    def __mul__(self, n):
        if n <= 0:
            raise ValueError("El mùltiplo debe ser mayor a cero")
        return Circle(self.radius * n)
    
    def __str__(self):
        return f"Circle with radius {self.radius}"

    pass
