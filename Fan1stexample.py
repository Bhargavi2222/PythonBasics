class Fan():
    def __init__(self):
        self.brand="USHA"
        self.color="White"
        self.cost=1800
        self.noOfBlades=3
    def on(self):
        print("Fan is On")
    def rotate(self):
        print("Fan is Rotating")
f1=Fan()
print(f1.brand)
print(f1.color)
print(f1.noOfBlades)
print(f1.cost)
f1.on()
f1.rotate()
