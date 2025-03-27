
from hotel import Hotel
from guest import Guest
from room import Room, SingleBedRoom, DoubleBedRoom
from reservation import Reservation
from service import Service
from loyaltyprogram import LoyaltyProgram




# Create Services
service1 = Service("Room Cleaning", 20)
service2 = Service("Breakfast", 15)
service3 = Service("Airport Shuttle", 30)

# Create a Hotel
hotel = Hotel("Royal Stay Hotel", "123 Luxury Lane, Cityville")
hotel.add_loyalty_program(10,"Free Dinner")
hotel.add_loyalty_program(30, "Free Night Stay")
hotel.add_loyalty_program(20, "25% Discount")

# Task 1
guest1 = Guest("Alice Johnson", "alice@example.com", "123-456-7890", "Gold")
guest2 = Guest("Bob Smith", "bob@example.com", "987-654-3210", "Silver")
guest3 = Guest("Charlie Davis", "charlie@example.com", "555-666-7777", "Platinum")

# Create Rooms
room1 = SingleBedRoom(101, 100, True)
room2 = SingleBedRoom(102, 110, True)
room3 = DoubleBedRoom(201, 150, True)
room4 = DoubleBedRoom(202, 160, True)
room5 = DoubleBedRoom(203, 170, True)

# Add Rooms to the Hotel
hotel.add_rooms([room1, room2, room3, room4, room5])

hotel.search_for_available_rooms()


# Guest booking reservations
guest1.book_reservation(room1,"3/20/2025","3/25/2025")
guest1.book_reservation(room2,"3/20/2025","3/25/2025")

# generating invoice for guest with 20% discount with 2 additional services
hotel.generate_invoice(guest1,20,[service1,service2])

guest1.view_reservations()

# 3 rooms available
hotel.search_for_available_rooms()

# reservation failed: guest 2 trying to book room 1 which is unavailable
guest2.book_reservation(room2,"3/27/2025","3/28/2025")

# reservation successful: guest 2 booking room3 which is available
guest2.book_reservation(room3,"3/27/2025","3/28/2025")

# generating invoice for guest2 with 5% discount with 1 additional service
hotel.generate_invoice(guest2,5,[service1,service2])

# now all of the guests trying to check their rewards
# guest 1 has 2 reservations so he will have all the 2 rewards
guest1.check_loyalty_rewards(hotel)

# guest 2 has only one reservation so he will have only "free dinner" reward
guest2.check_loyalty_rewards(hotel)

# guest 3 has no reservations so he is not eligible for any rewards
guest3.check_loyalty_rewards(hotel)


