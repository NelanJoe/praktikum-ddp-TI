animals = ["Kucing", "Ayam", "Gorilla"]

# # Rest / Spread Operator
newAnimal = "Guguk"

animals = [*animals, newAnimal]

print(animals)

# Rest parameter
def getDataAnimals(*animals):
    for animal in animals:
        print(animal)

getDataAnimals("Kucing", "Ayam", "Gorilla", "Guguk")

# Operator Number pakai rest Param
def addNumber(*numbers):
    result = 0
    for number in numbers:
        result += number

    print(result)


addNumber(10, 5, 6, 7, 8)