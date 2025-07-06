class animal:
    def __init__(self,name):
        self.name = name
    def speaks(self):
        print(f"{self.name} makes a sound.")

class dog(animal):
    def __init__(self,name,nature):
        super().__init__(name)
        self.nature = nature
    def speaks1(self):
        print(f"{self.name} barks and has {self.nature} nature")

obj_ani = animal("Dog")
print(obj_ani.name)
obj_ani.speaks()
obj_dog = dog("Bunny","friendly")
obj_dog.speaks1()