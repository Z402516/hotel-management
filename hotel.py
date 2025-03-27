class Hotel:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__guests = []
        self.__rooms = []
        self.__loyalty_program = LoyaltyProgram()
        self.__reservations = []

    def add_rooms(self,rooms):
        self.__rooms.extend(rooms)

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
        '''
        This method iterates over the list of rooms and checks if the room is available then it
        displays the information of the room.
        '''
        print("\n*****    Available Rooms     *****")
        for room in self.__rooms:
            if room.get_availability():
                print("Room {}  Type : {}".format(room.get_room_number(),room.get_room_type()))


    def generate_invoice(self, guest, discount, services):
        '''
        This method will check the reservations for a guest and takes the additional services which the guest
        requested. It also takes in the discount which should be applied. THis method then displays all the
        reservation details, calculates nigh stays, calculates price per reservation and finally total
        amount which the user must pay after discount.

        '''

        reservations = len(guest.get_reservations())
        print("\n*****    Invoice     *****")
        print("{} Total Reservations for {}".format(guest.get_name(),reservations))
        total_price = 0
        for reservation in guest.get_reservations():
            print("Reservation from {} to {}".format(reservation.get_check_in(),reservation.get_check_out()))
            check_in = reservation.get_check_in()
            check_out = reservation.get_check_out()
            check_in_date = datetime.strptime(check_in, "%m/%d/%Y")
            check_out_date = datetime.strptime(check_out, "%m/%d/%Y")

            days_stayed = (check_out_date - check_in_date).days
            reservation_price = days_stayed * reservation.get_room().get_per_night_price()
            print("Reservation Nights :",days_stayed)
            print("Reservation Price :",reservation_price)
            total_price += reservation_price

        for service in services:
            print("Service Name :",service.get_service_name())
            print("Service Price :",service.get_service_price())
            total_price += service.get_service_price()

        print("Total Price :",total_price)
        if discount == 0:
            discount_amount = 0
        else:
            discount_amount = total_price*(discount/100)

        print("Discount Amount :",discount_amount)
        print("Bill After Discount :",total_price-discount_amount)


    def add_loyalty_program(self,points,reward):
        self.__loyalty_program.add_program(points,reward)
