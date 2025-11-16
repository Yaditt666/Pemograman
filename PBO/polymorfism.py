# Duck Typing Example
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def move(self):
        return f"{self.brand} sedang berjalan di jalan"

class Airplane:
    def __init__(self, airline):
        self.airline = airline
    
    def move(self):
        return f"{self.airline} sedang terbang di udara"

class Boat:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return f"{self.name} sedang berlayar di laut"

def start_journey(vehicle):
    """Fungsi yang bekerja dengan objek apapun yang memiliki method move()"""
    return vehicle.move()

# Testing Duck Typing
def demo_duck_typing():
    print("\n=== DUCK TYPING DEMO ===")
    
    car = Car("Toyota")
    airplane = Airplane("Garuda Indonesia")
    boat = Boat("Kapal Laut")
    
    vehicles = [car, airplane, boat]
    
    for vehicle in vehicles:
        print(start_journey(vehicle))