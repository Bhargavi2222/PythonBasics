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
h2=h1
h3=h2  #h2=h3 gives error
h3.addr="Mysore"
print(h1.name,'\n',h2.age)
print(h3.mob,'\t',h2.addr)