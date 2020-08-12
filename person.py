class Person:

    def __init__(self, name="", surname="", age=None):
        self._name = name.upper()
        self._surname = surname.upper()
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.upper()

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname.upper()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


if __name__ == "__main__":
    person1 = Person("mariano", "Saez", 20)
    print(person1.name, person1.surname, person1.age)
