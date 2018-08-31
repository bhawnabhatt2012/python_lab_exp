print("python programming....")
#parent class
class Polygon:
    no_of_sides=0
    sides=[]
    def __init__(self,no_of_sides):
        self.no_of_sides=no_of_sides
        for x in range(0,no_of_sides):
            self.sides.append(0)
    def input_sides(self):
        for x in range(0,self.no_of_sides):
            z=int(input("ENTER %d side" %(x)))
            self.sides[x]=z
        return
    def print_sides(self):
        print("SIDES OF TRIANGLE ARE :- ")
        print(self.sides)
        return
#child parent
class Triangle(Polygon):
    def __init__(self):
        Polygon(3)
        self.no_of_sides = 3
    def find_area(self):
        self.input_sides()
        self.print_sides()

        s=sum(self.sides)/2
        print("area of triangle:-")
        print(s)


        return
T1=Triangle()
T1.find_area()












