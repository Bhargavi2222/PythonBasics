class Hero():
    def __init__(self):
      self.name="Darshan"
      self.age=46
      self.height=6.3
    def act(self):
        print("He is an Actor")
    def dance(self):
        print("He is a good Dancer")
h1=Hero()
print(h1.height)
h1.mob=987564123
print(h1.mob)
h2=h1   #h1=h2 gives error
print(h1.age)
h1.act()
h2.dance()


