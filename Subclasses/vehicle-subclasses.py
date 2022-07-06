class Vehicle:
    """Vehicle class"""
    def __init__(self, year, color, numberofWheels, capacity):
        self._year = year
        self._color = color
        self._numberofWheels = numberofWheels
        self._capacity = capacity

    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color
    
    @property
    def numberofWheels(self):
        return self._numberofWheels

    @property
    def capacity(self):
        return self._capacity

    @year.setter
    def year(self, new_year):
        self._year = new_year

    @color.setter
    def author(self, new_author):
        self._color = new_color

    @numberofWheels.setter
    def numberofWheels(self, new_numberofWheels):
        self._numberofWheels = new_numberofWheels

    @capacity.setter
    def capacity(self, new_capacity):
        self._capacity = new_capacity

    def start(self):
        print('Starting')
    
    def stop(self):
        print('Stopping')
    
    def move(self):
        print('Moving')

class Car(Vehicle):
    """Car class, inheriting from Vehicle"""
    def __init__(self, year, color, numberofWheels, capacity, make, model, miles, mpg):
        super().__init__(year, color, numberofWheels, capacity)
        self.__make = make
        self.__model = model
        self.__miles = miles
        self.__mpg = mpg

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def miles(self):
        return self.__miles
    
    @property
    def mpg(self):
        return self.__mpg

    @make.setter
    def make(self, new_make):
        self._make = new_make
    
    @model.setter
    def model(self, new_model):
        self._model = new_model

    @miles.setter
    def miles(self, new_miles):
        self._miles = new_miles
    
    @mpg.setter
    def mpg(self, new_mpg):
        self._mpg = new_mpg
    
    def brake(self):
        print('braking')

class Bicycle(Vehicle):
    """Bicycle class, inheriting from Vehicle"""
    def __init__(self, year, color, numberofWheels, capacity, brand):
        super().__init__(year, color, numberofWheels, capacity)
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

    def wheelie(self):
        print('Doing a Wheelie')
    
    def brake(self):
        print('Braking')

class Boat(Vehicle):
    """Boat class, inheriting from Vehicle"""
    def __init__(self, year, color, numberofWheels, capacity, brand, typeofBoat):
        super().__init__(year, color, numberofWheels, capacity)
        self.__brand = brand
        self._typeofBoat = typeofBoat

    @property
    def brand(self):
        return self.__brand

    @property
    def typeofBoat(self):
        return self._typeofBoat
    
    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

    @typeofBoat.setter
    def typeofBoat(self, new_type):
        self._typeofBoat = new_type
    
    def brake(self):
        print('Braking')

class HotAirBalloon(Vehicle):
    """Hot Air Balloon class, inheriting from Vehicle"""
    def __init__(self, year, color, numberofWheels, capacity, size):
        super().__init__(year, color, numberofWheels, capacity)
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def brand(self, new_brand):
        self._size = new_size

    def rise(self):
        print('Rising')
    
    def fall(self):
        print('Falling')