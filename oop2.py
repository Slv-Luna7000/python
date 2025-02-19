
class Cars:
    def __init__(self,make, model, color,YOM ):
        self.make=make
        self.model=model
        self.color=color
        self.YOM=YOM
    def display(self):
        print(f"The make of my dream car is:{self.make}, model is :{self.model}, its color should be: {self.color}, and the YOM :{self.YOM}")

mycar=Cars(make= "McLaren",model="Lexus IS",color="Blue",YOM=2012)
mycar.display()
mycar1=Cars(make= "Nissan", model="L RX",color="Black",YOM=2015)
mycar1.display()
mycar2=Cars(make= "BMW", model="Porsche",color="Red",YOM=2010)
mycar2.display()
mycar3=Cars(make= "Ford",model="Mustang",color="Silver",YOM=2020)
mycar3.display()
mycar4=Cars(make= "Toyota",model="Avensis",color="Violet",YOM=2005)
mycar4.display()

