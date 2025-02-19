class Dad:
    def __init__(self,color,hobby):
        self.color=color
        self.hobby=hobby
class Mum:
    def __init__(self,color,hobby):
        self.color=color
        self.hobby=hobby
# child class, subclass
class Boy(Dad):
    def boyinherits(self):
        print(f"Boys inherits {self.color} and the {self.hobby}")
class Girl(Mum):
    def girlinherits(self):
        print(f"Girls inherits {self.color},and {self.hobby}")

# Instance
myobj=Boy(color="African descent", hobby="Watching soccer from the Dad")
myobj.boyinherits()
myobj2=Girl(color="Light Asian descent",hobby="Loves cooking and baking")
myobj2.girlinherits()
