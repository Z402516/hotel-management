class Room:
    def __init__(self, room_number, per_night_price, availability, room_type):
        self.__room_number = room_number
        self.__per_night_price = per_night_price
        self.__availability = availability
        self.__room_type = room_type

    def get_room_number(self):
        return self.__room_number

    def get_per_night_price(self):
        return self.__per_night_price

    def get_availability(self):
        return self.__availability

    def get_room_type(self):
        return self.__room_type

    def set_room_number(self, room_number):
        self.__room_number = room_number

    def set_per_night_price(self, price):
        self.__per_night_price = price

    def set_availability(self, availability):
        self.__availability = availability

    def set_room_type(self, room_type):
        self.__room_type = room_type


class SingleBedRoom(Room):
    def __init__(self, room_number, per_night_price, availability):
        super().__init__(room_number, per_night_price, availability, "Single Bed Room")


class DoubleBedRoom(Room):
    def __init__(self, room_number, per_night_price, availability):
        super().__init__(room_number, per_night_price, availability, "Double Bed Room")
