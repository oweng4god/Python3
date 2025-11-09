class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100 #base fare per person
#Child class
class Bus(Vehicle):
    def fare(self):
        #Get base fare from parent class using super()
        total_fare = super().fare()
        #Add 10% extramchange for maintenance
        total_fare += total_fare *0.10
        return total_fare
#Example usage
school_bus = Bus("School Volvo", 12, 50)
print(f"Total Bus fare is: Rs {school_bus.fare()}")           