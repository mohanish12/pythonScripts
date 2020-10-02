class Person:
    def __init__(self, name, eyecolour, age):
        self.name = name
        self.eyecolour = eyecolour
        self.age = age

class Name:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


myPerson = Person(Name("David", "Joyner"), "brown", 26)
print(myPerson.name.firstName)
print(myPerson.name.lastName)
print(myPerson.eyecolour)
print(myPerson.age)
