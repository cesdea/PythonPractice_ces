import object_Person
class Student(object_Person.Person):
    def study(self):
        print('열공 중..')

studnet=Student()
studnet.study()
studnet.eat()
print(studnet.mouth)
