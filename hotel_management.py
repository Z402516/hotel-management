
class Hotel:
    def __init__(self, name, address, loyalty_program):
        self.__name = name
        self.__address = address
        self.__guests = []
        self.__rooms = []
        self.__loyalty_program = loyalty_program
        self.__reservations = []

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_guests(self):
        return self.__guests

    def get_rooms(self):
        return self.__rooms

    def get_loyalty_program(self):
        return self.__loyalty_program

    def get_reservations(self):
        return self.__reservations

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_loyalty_program(self, loyalty_program):
        self.__loyalty_program = loyalty_program

    def search_for_available_rooms(self):
        pass

    def make_reservation(self):
        pass

    def generate_invoice(self, reservation_id, discount, services):
        pass

    def add_loyalty_points(self, guest, points):
        pass


class Guest:
    def __init__(self, name, email, phone_number, loyalty_status, loyalty_points=0):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__loyalty_status = loyalty_status
        self.__loyalty_points = loyalty_points
        self.__reservations = []

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def get_loyalty_status(self):
        return self.__loyalty_status

    def get_loyalty_points(self):
        return self.__loyalty_points

    def get_reservations(self):
        return self.__reservations

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_loyalty_status(self, loyalty_status):
        self.__loyalty_status = loyalty_status

    def set_loyalty_points(self, points):
        self.__loyalty_points = points

    def view_reservations(self):
        pass

    def check_loyalty_rewards(self, loyalty_program):
        pass

    def request_service(self, service):
        pass

    def feedback(self):
        pass


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


class Reservation:
    def __init__(self, reservation_id, room_number, check_in, check_out):
        self.__reservation_id = reservation_id
        self.__room_number = room_number
        self.__check_in = check_in
        self.__check_out = check_out

    def get_reservation_id(self):
        return self.__reservation_id

    def get_room_number(self):
        return self.__room_number

    def get_check_in(self):
        return self.__check_in

    def get_check_out(self):
        return self.__check_out

    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    def set_room_number(self, room_number):
        self.__room_number = room_number

    def set_check_in(self, check_in):
        self.__check_in = check_in

    def set_check_out(self, check_out):
        self.__check_out = check_out

