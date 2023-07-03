class Magari:
    def __init__(self, modelname, color, year, capacity):
        self.model = modelname
        self.mycolor = color
        self.myyear = year
        self.cc=capacity

    def onyesha(self):
        print(self.model, self.myyear, self.mycolor,self.cc)


# create an object
myobj = Magari("Toyota", "white", 2009, "2900cc")
Object2= Magari("Range","black",2022, "2950cc")
Object2.onyesha()
