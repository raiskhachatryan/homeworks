class Person:
    def __init__(self, name, last_name, age, gender, student):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student

    def Greeting(self, second_person):
        print('Welcome dear', second_person)


    def Goodbye(self):
        print('Bye everyone', )


    def Favourite_num(self, num1):
        print('My favourite number is', num1)



p_1 = Person('Raisa', 'Khachatryan', '21', 'f', True )

p_1.Greeting(input('Input name! ') )
p_1.Goodbye()
num1 = input('avourite number! ' )
p_1.Favourite_num(num1)










