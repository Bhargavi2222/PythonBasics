class Student():
    def __init__(self):
        self.Name="Bhargavi"
        self.Age=20
        self.USN="1VK20IS004"
        self.Mobile=987654321

    def eat(self):
        print("Student is Eating")
    def sleep(self):
        print("Student is sleeping")
    def study(self):
        print("Student is studying")
s1=Student()
print(s1.Name)
print(s1.Age)
print(s1.USN)
print(s1.Mobile)
s1.eat()
s1.sleep()
s1.study()
