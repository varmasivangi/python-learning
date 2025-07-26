
class Vehicle:
#constructor
    def __init__(self,color,cost):
        self.color = color
        self.cost = cost


    def assign_properties(self,color,cost):
        self.color = color
        self.cost = cost


    def show_vehicle_details(self):
        print("vehicle color : ",self.color)
        print("vehicle cost : ",self.cost)


# v1 = Vehicle("green",10000)

# v1.assign_properties("red","5000K")
# v1.show_vehicle_details()



class Car(Vehicle):

    def __init__(self, color, cost,tyres,hp):
        super().__init__(color, cost)
        self.tyres =tyres
        self.hp = hp

    def assign_car_details(self):
       
        print(self.color)
        print(self.tyres)
        print(self.hp)




v2 = Car("pink","8000","4tyres",'350cc')

v2.assign_car_details()