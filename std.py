class Student():
    data = []
    def __init__(self):
        self.register()

    def register(self):
        print('Welcome')
        x = int(raw_input("Press 1 for register\n"))
        if x == 1:
            self.add()
        else:
            print("Try again")
            self.register()

    def add(self):
        # self.data = []
        for i in range(0, 1):
            x = raw_input('Enter the Student name: ')
            self.data.append(x)
            self.stored()

    def update(self):
        print("Enter stdent name to be change")
        n=raw_input()
        new=raw_input("Enter new name")
        for i in range(0, end)
            if data[i]==n
                data[i]=new
            else:
                pass




    def stored(self):
        x = int(raw_input("< 1 > View \n< 2 > Add \n< 3 > Update"))
        if x == 1:
            self.view()
        elif x == 2:
            self.add()
        elif x == 3:
            self.update()
        else
            exit

    def view(self):
        
        print(self.data)
       
        

p1 = Student()

