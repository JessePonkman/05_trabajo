from person import Person
from personService import PersonService


class App():
    def menu(self):
        print("\n1. Agregar una Persona")
        print("2. Listar Personas")
        print("3. Modificar una Persona")
        print("4. Borrar una Persona")
        print("5. Ejercicios")
        return int(input("Ingrese una opcion: "))


if __name__ == '__main__':
    app = App()
    personService = PersonService()

    while True:
        opc = app.menu()
        if opc == 1:
            personService.add_person()
        if opc == 2:
            print("\n", personService.get_personList())
        if opc == 3:
            personService.update_person()
        if opc == 4:
            personService.delete_person()
        if opc == 5:
            # Agregamos una persona **A modo de mostrar las opciones
            # del menu cambie un poco la creacion de los objetos
            # pero manteniendo los ejemplos como se dieron
            p1 = Person()
            p1.name = 'federico'
            p1.surname = 'gonzalez'
            p1.age = '20'
            personService.add_person(p1)

            continuar = input("\nPresione ENTER para continuar...\n")

            # Agregamos una persona
            p1 = Person()
            p1.name = 'claudio'
            p1.surname = 'pico'
            p1.age = '33'
            personService.add_person(p1)

            continuar = input("\nPresione ENTER para continuar...\n")

            # Agregamos al hermano **********************
            p1 = Person('Nicolas', 'Pico', 40)
            personService.add_person(p1)

            continuar = input("\nPresione ENTER para continuar...\n")

            print(personService.get_personList())
            # {0: {'_name': 'FEDERICO', '_surname': 'GONZALEZ', '_age': '20'},
            #  1: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 30},
            #  2: {'_name': 'NICOLAS', '_surname': 'PICO', '_age': 30}}

            continuar = input("\nPresione ENTER para continuar...\n")

            # Update FEDERICO
            personService.update_person(0)

            continuar = input("\nPresione ENTER para continuar...\n")

            print(personService.get_personList())

            continuar = input("\nPresione ENTER para continuar...\n")

            # Delete person
            personService.delete_person(2)

            continuar = input("\nPresione ENTER para continuar...\n")

            print(personService.get_personList())
            # {0: {'_name': 'FEDERICO','_surname': 'GONZALEZ', '_age': '20'},
            #  1: {'_name': 'NICOLAS', '_surname': 'NICOLAS', '_age': 41}}

            continuar = input("\nPresione ENTER para continuar...\n")
        if opc < 1 or opc > 5:
            break
