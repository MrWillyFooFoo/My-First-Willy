from abc import ABC, abstractmethod 
 
 
class Animal(ABC): 
    def __init__(self, _name, _age): 
        self.name = _name 
        self.age = _age 
 
    @abstractmethod 
    def speak(self): 
        return f"" 
 
    @abstractmethod 
    def __str__(self): 
        pass 
 
 
class Dog(Animal): 
    def __init__(self, name, age, _breed): 
        super().__init__(name, age) 
        self.breed = _breed 
 
    def speak(self): 
        return "Woof!" 
 
    def __str__(self): 
        return f"{self.name} is a {self.age}-year-old dog, and says Woof!" 
 
 
class Cat(Animal): 
 
    def __init__(self, name, age, _colour): 
        super().__init__(name, age) 
        self.colour = _colour 
 
    def speak(self): 
        return "Meow!" 
 
    def __str__(self): 
        return f"{self.name} is a {self.age}-year-old cat, and says Meow!" 
 
 
class AnimalShelter: 
    def __init__(self): 
        self.shelter = [] 
 
    def add_animal(self, *args): 
        for x in args: 
            if isinstance(x, Animal): 
                self.shelter.append(x) 
            else: 
                return "Not a valid class" 
 
    def get_animals_by_type(self, obj): 
        animallist = [] 
        for x in self.shelter: 
            if isinstance(x, type(obj)): 
                animallist.append(x) 
 
        return animallist 
 
    def get_animals_by_age(self, minage, maxage): 
        animallist = [] 
        for x in self.shelter: 
            if minage <= x.age <= maxage: 
                animallist.append(x) 
 
        return animallist 
 
    def get_shelter(self): 
        return self.shelter 
 
 
dog1 = Dog("Fido", 5, "Labrador") 
cat1 = Cat("Fluffy", 3, "White") 
dog2 = Dog("Buddy", 2, "Golden Retriever") 
cat2 = Cat("Whiskers", 2, "Black") 
 
shelter = AnimalShelter() 
shelter.add_animal(dog1, dog2, cat1, cat2) 
 
print(shelter.get_animals_by_type(cat1)) 
 
print(shelter.get_animals_by_age(1, 100)) 