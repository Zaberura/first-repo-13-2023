class Helicopter:
    def __init__(self, passengers=0, name="", max_speed=0, public_number=0, public_string=""):

        self.__passengers = passengers
        self.__name = name
        self.__max_speed = max_speed

        self.public_number = public_number
        self.public_string = public_string

    def get_passengers(self):
        return self.__passengers

    def get_name(self):
        return self.__name

    def get_max_speed(self):
        return self.__max_speed

    def set_passengers(self, passengers):
        self.__passengers = passengers

    def set_name(self, name):
        self.__name = name

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def __str__(self):
        return f"Вертоліт: {self.__name}, Пасажирів: {self.__passengers}, Максимальна швидкість: {self.__max_speed}"

    def __repr__(self):
        return f"Вертоліт({self.__passengers}, '{self.__name}', {self.__max_speed})"

    def __del__(self):
        print(f"Об'єкт {self.__name} було видалено.")


# Головний метод
def main():
    helicopter1 = Helicopter(passengers=6, name="Bell 206", max_speed=120,
                             public_number=42, public_string="First Helicopter")
    helicopter2 = Helicopter(passengers=4, name="Robinson R44", max_speed=130,
                             public_number=55, public_string="Second Helicopter")
    helicopter3 = Helicopter(passengers=8, name="Sikorsky S-92", max_speed=190,
                             public_number=33, public_string="Third Helicopter")

    print(helicopter1)
    print(helicopter2)
    print(helicopter3)

    del helicopter2



if __name__ == "__main__":
    main()

