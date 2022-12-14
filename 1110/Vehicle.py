class Vehicle:
    def __init__(self,make,model,color,price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price

    def setMake(self,make):
        self.make = make

    def getMake(self):
        return self.make

    def getDesc(self):
        return "차량=("+str(self.make)+","+ str(self.color) +','+str(self.price)+')'


class Truck(Vehicle):
    def __init__(self,make,model,color,price,payload):
        super().__init__(make,model,color,price)
        self.payload = payload

    def setPayload(self,payload):
        self.payload = payload
    def getPayload(self):
        return self.payload

def main():
    myTruck = Truck("Tisla","Model S","white",10000,20000)
    myTruck.setMake("Tesla")
    myTruck.setPayload(3000)
    print(myTruck.getDesc())
main()