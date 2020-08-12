from repository import Repository
from person import Person


class PersonService():
    def get_personList(self):
        print("\n--------Lista de Personas--------")
        return Repository.person

    def createPerson(self):
        name = input("\nIngrese el nombre de la Persona: ")
        surname = input("Ingrese el apellido de la Persona: ")
        age = int(input("Ingrese la edad de la Persona: "))
        person = Person(name, surname, age)
        return person

    def add_person(self, person=None):
        print("\n--------Agregar Persona--------")
        if person is None:
            person = self.createPerson()
        for key in Repository.person:
            lastKey = key
        lastKey += 1
        Repository.person[lastKey] = person.__dict__
        print("\n%s ha sido añadido!" % person.name)

    def update_person(self, key=None, opc=None):
        print("\n--------Modificar Persona--------")
        if key is None:
            key = int(input("\nIngrese el codigo de la persona: "))
        person = Repository.person[key]
        print("\nEsta es la persona: %s" % person)
        print("\n1. Nombre")
        print("2. Apellido")
        print("3. Edad")
        if opc is None:
            opc = int(input("\nIngrese el atributo que desea modificar: "))
        modify = input("\nIngrese el nuevo valor: ")
        if opc == 1:
            person['_name'] = modify.upper()
        if opc == 2:
            person['_surname'] = modify.upper()
        if opc == 3:
            person['_age'] = int(modify)
        print("\nModificacion exitosa!\n%s" % person)

    def delete_person(self, key=None):
        print("\n--------Eliminar Persona--------")
        if key is None:
            key = int(input("\nIngrese el codigo de la persona: "))
        opc = input("\nSeguro quiere borrar a %s del diccionario? Y/N\n"
                    % Repository.person[key]['_name'])
        if opc.upper() == "Y":
            del Repository.person[key]
            print("\nSe elimino del diccionario correctamente!\n")
