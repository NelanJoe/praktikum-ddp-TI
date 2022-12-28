# Class Animal
class Animal:
    '''
        * Property :=> Variable
    '''
    name = ""
    age = 0

    '''
        * Constructor :=> yang nempel di class Animal sebagai parameter yang harus di isi
        * Constructor dengan default parameter
    '''
    def __init__(self, name="kucing", age=2):
        self.name = name
        self.age = age
    
    '''
        * Method / Function
    '''
    def sayAnimal(self):
        print(f"Hallo nama saya {self.name}, usia saya {self.age} tahun")
    


kucing = Animal()
kucing.sayAnimal()
