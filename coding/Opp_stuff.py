class Vehicle:
    def __init__(self, name, max_speed, make, model, mileage):
        self.name = name
        self.max_speed = max_speed
        self.make = make
        self.model = model
        self.mileage = mileage
        
    def __str__(self):
       return self.name + " is " + self.color + " and goes at a max speed of " + str(self.max_speed) + ". Its make is " + self.make + 'and its model is ' + self.model + '. Finally its mileage is ' + str(self.mileage) + '.'
    
    def Seating(self):
        input


    def Charge(self):




class Bus(Vehicle):




car = Vehicle('mustang', 'white', 110, 'Ford Motor Company', '1990 ford Mustang', 22434,)
print(car)
