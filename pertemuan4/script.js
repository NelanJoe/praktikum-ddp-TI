// let animals = ["Kucing", "Ayam", "Gorilla"]

// // Spread Operator

// animals = [...animals, "Guguk"]

// console.log(animals);

// Rest Parameter
function getDataAnimals(...animals){
    for(const animal of animals){
        console.log(animal);
    }
}


getDataAnimals("Kucing", "Ayam", "Gorilla")