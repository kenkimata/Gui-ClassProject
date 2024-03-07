class Pet() :
    name = None
    fullness = 0

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + " is eating " + food + "...")
        if food == "steak":
            self.fullness == self.fullness + 50
        elif food == "juice":
            self.fullness == self.fullness + 2
        elif food == "dog food":
            self.fullness == self.fullness + 20

    
        print(self.name, "is now", self.fullness, "% full")


pet_owner_name = input("what is your name")
print("Hello, ", pet_owner_name)

pet_1 = Pet("dog")

