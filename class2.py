class people():
    def __init__(self, name, gender, age):
        self.myname=name
        self.mygender=gender
        self.myage=age

    def show(self):
        print(self.myname, self.mygender, self.myage)

person1=people("Jane","female", 26)
person1.show()
person2=people("John","Male", 87)
person2.show()
person3=people("Annah","Female",44)
person3.show()