class Reservation:
    def __init__(self, room, check_in, check_out):
        self.__room = room
        self.__check_in = check_in
        self.__check_out = check_out


    def get_room_number(self):
        return self.__room.get_room_number()

    def get_room(self):
        return self.__room

    def get_check_in(self):
        return self.__check_in

    def get_check_out(self):
        return self.__check_out

    def set_check_in(self, check_in):
        self.__check_in = check_in

    def set_check_out(self, check_out):
        self.__check_out = check_out

    def reservation_details(self):
        print("Reservation Room Number :",self.__room.get_room_number())
        print("Reservation Check in :",self.get_check_in())
        print("Reservation Check out :",self.get_check_out())
