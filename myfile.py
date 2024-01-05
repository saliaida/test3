


class Person:
    a = 1
    _b = 2
    __c = 3
    def __init__(self):
        self.score1 = 10
        self._score2 = 20
        self.__score3 = 30
        
class Student(Person):
    def __init__(self,fname,lname,age):
        Person.__init__(self)
        self.fname = fname
        self.lname = lname
        self.age = age
    def __str__(self):
        # lst = [self.fname,self.lname,self.age]
        return f'-{self.fname}\t{self.lname}\n\t{self.age}'
    def __add__(self, other):
        return self.age + other.age


s1 = Student('ali', 'ahmadi', 20)
s2 = Student('reza', 'rezayee', 18)

print(s1.__add__(s2))
print(s1 + s2)
print(s1 / s2)


print(s1)
print('**********')




# def _func():
#     print('*********')

# def __func():
#     print('============')



