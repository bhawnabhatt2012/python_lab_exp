class Time:
    hour=0
    minute=0
    seconds=0
    def input_values(self):
        self.hour=int(input("ENTER HR"))
        self.minute=int(input("ENTER MINU"))
        self.seconds=int(input("ENTER SECONDS"))
        return
    def print_details(self,V1):
        print("YOUR RESULT:%d:%d:%d" %(V1.hour,V1.minute,V1.seconds))
        return
    def __add__(self,V2):
        V3=Time()
        V3.hour=self.hour+V2.hour
        V3.seconds=self.seconds+V2.seconds
        V3.minute=self.minute+V2.minute
        while(V3.seconds>=60):
            V3.seconds=V3.seconds-60
            V3.minute = V3.minute + 1
        while(V3.minute>=60):
            V3.minute = V3.minute - 60
            V3.hour=V3.hour+1
        while(V3.hour>=24):
            V3.hour=V3.hour-24
        return V3
    def __sub__(self, V2):
        V3=Time()
        V3.hour=(self.hour-V2.hour)
        V3.seconds=(self.seconds-V2.seconds)
        V3.minute = (self.minute - V2.minute)
        while(V3.seconds<=0):
            V3.seconds=V3.seconds+60
            V3.minute=V3.minute-1
        while(V3.minute<=0):
            V3.minute+=60
            V3.hour-=V3.hour-24

        return V3

V1=Time()
V3=Time()
V2=Time()
V1.input_values()
V2.input_values()
V3=V1+V2
print("ON ADDING")
V3.print_details(V3)
V4=Time()
print("ON SUB")
V4=V1-V2
V4.print_details(V4)
