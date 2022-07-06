class Animal:
    """Animal class"""
    def __init__(self, species, age, gender):
        self._species = species
        self._age = age
        self._gender = gender
    @property
    def species(self):
        return self._species

    @property
    def age(self):
        return self._age
    
    @property
    def gender(self):
        return self._gender
    
    @species.setter
    def species(self, new_species):
        self._species = new_species

    @age.setter
    def age(self, new_age):
        self._age = new_age

    def move(self):
        print('Moving')
    
    def eat(self):
        print('Eating')
    
    def die(self):
        print('Dying')
    
    def reproduce(self):
        print('reproducing')

class Fish(Animal):
    def swim(self):
        print('Swimming')

class Snake(Animal):
    """Snake class, inheriting from Animal"""
    def __init__(self, species, age, gender, poisonStatus):
        super().__init__(species, age, gender)
        self.__poisonStatus = poisonStatus

    @property
    def poisonStatus(self):
        return self.__poisonStatus
    
    @poisonStatus.setter
    def poisonStatus(self, new_poisonStatus):
        self.__poisonStatus = new_poisonStatus

    def shed(self):
        print('Shedding')
    
    def bite(self):
        print('Biting')

class Person(Animal):
    """Snake class, inheriting from Animal"""
    def __init__(self, species, age, gender, hairColor):
        super().__init__(species, age, gender)
        self.__hairColor = hairColor

    @property
    def hairColor(self):
        return self.__hairColor
    
    @hairColor.setter
    def hairColor(self, new_hairColor):
        self.__hairColor = new_hairColor

    def talk(self):
        print('Talking')