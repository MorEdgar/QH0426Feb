class Human:
    MAX_ENERGY=100 #class attribute
    def __init__(self, age=0, name="Human", energy=MAX_ENERGY):   #instance attribute
        self.name=name
        self.age=age
        self.energy=Human.MAX_ENERGY

    def display(self):
        print(f"Iam {self.name} age{self.age}")
    if(__name__=="__main__"):
     human=Human()
     human.display()



