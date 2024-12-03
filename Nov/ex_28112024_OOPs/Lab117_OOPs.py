class Person:
    id=None
    name=None
    gender=None

    def walk(self):
        print("I can walk")
    def talk(self,name):
        print("I am " + name + ". I can talk in Hindi and English")

vaish= Person()
vaish.walk()
vaish.talk("Vaishnavi")
