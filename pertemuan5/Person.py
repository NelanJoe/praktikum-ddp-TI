class Person:
    # Property
    name = ""
    age = 0
    address = ""
    
    # Getter name
    def getName(self):
        return self.name

    # Method / Function
    def sayHello(self):
        print(f"Hallo nama saya {self.name}, saya berusia {self.age}, dan saya beralamatkan di {self.address}")

    
    def helloWorld(self, place):
        print(f"Hallo nama saya {self.name} saya ada di {place}")


class Animal:
    name = ""

    def getName(self):
        print(f"Nama saya {self.name}")


'''
    Instance Object / Hasil dari pembuatan class
'''
nelan = Person()

nelan.name = "Nelan"
nelan.age = 20
nelan.address = "Bogor, Indonesia"


guguk = Animal()
guguk.name = "Guguk"
guguk.getName()