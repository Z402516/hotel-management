from reservation import Reservation

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

    def book_reservation(self,room,check_in,check_out):
        '''
        This method will take the necessary details from the guest and books the reservation based on the room
        availability. it also adds 10 points per reservation.

        '''
        res = Reservation(room,check_in,check_out)
        if room.get_availability():
            self.__reservations.append(res)
            print("Reservation on {} was successful".format(check_in))
            print("Notification is sent to {}".format(self.__email))
            self.__loyalty_points += 10
            room.set_availability(False)

        else:
            print("Reservation Failed Room {} not available".format(room.get_room_number()))

    def view_reservations(self):
        '''
        This method will loop over all the reservations for the guest and displays their details.
        :return:
        '''
        print("\n*****    Viewing Reservations for {}     *****".format(self.get_name()))
        res_number = 0
        for res in self.__reservations:
            res_number += 1
            print("Details for Reservation",res_number)
            res.reservation_details()

    def cancel_reservation(self,room_number):
        '''
        This method takes in the room number and checks if the user has the reservation booked for this room.
        if found it cancels the reservation.
        :param room_number:
        :return:
        '''
        cancelled = False
        for i in self.__reservations:
            if room_number == i.get_room_number():
                print("Reservation for room",i.get_room_number(),"is cancelled.")
                self.__reservations.remove(i)
                cancelled = True
                break

        if not cancelled:
            print("Reservation with this Room Number Not Found.")

    def check_loyalty_rewards(self, hotel):
        '''
        This method will display what are the loyalty rewards the customer is eligible for.
        :param loyalty_program:
        :return:
        '''
        print("\n*****      Loyalty Rewards check for {}    *****".format(self.get_name()))
        print("Loyalty Points :",self.__loyalty_points)
        loyalty_program = hotel.get_loyalty_program()
        rewards = loyalty_program.get_eligible_rewards(self)
        print("Your Rewards :",rewards)
