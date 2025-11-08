class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.pi = 3.14
    def area(self):
        return self.pi * self.radius ** 2
    def preimeter(self):
        return 2 * self.pi * self.radius

r = float(input("Enter the radius of the circle: "))
c = Circle(r)

print(f"Area of circle: {c.area():.2f}")
print(f"Perimetr of circle: {c.perimrter():.2f}")