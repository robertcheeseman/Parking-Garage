class ParkingGarage():
    def __init__(self, capacity):
        self.tickets = []
        self.parkingSpaces = []
        self.currentTicket = {}
        self.capacity = capacity

    def takeTicket(self):
        if self.parkingSpaces == []:
            print(f"I'm sorry, there is no parking spaces avaliable")
        else:
            print("Thank you for requesting a ticket, Have a Great Day!\n")
            print(f"You have ticket {self.tickets[0]}")
            del(self.tickets[0])
            del(self.parkingSpaces[0])
            print(f"There is {len(self.parkingSpaces)} parking spaces left!")
            print(self.parkingSpaces)
        
        # decrease amount of tickets available by 1
        # decrease amount of parking spaces available by 1
        pass

    def payForParking(self):
        # Display an input that waits for an amount from the user and store it in a variable
        # If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
        # This should update the "currentTicket" dictionary key "paid" to True
        pass

    def leaveGarage(self):
        # If the ticket has been paid, display a message of "Thank You, have a nice day"
        # If the ticket has not been paid, display an input prompt for payment
        # Once paid, display message "Thank you, have a nice day!"
        # Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        # Update tickets list to increase by 1 (meaning add to the tickets list)
        pass

park = ParkingGarage(5)

def runner():
    print("\n+++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++\n")
    print("Hello.  Welcome to the Parking Garage.\n")
    for ticket in range(1, park.capacity + 1):
        park.tickets.append(ticket)
        park.parkingSpaces.append(ticket)
        park.currentTicket[int(ticket)] = False
    while True:
        print("Please select from the following options:")
        user_input = input(f'  [1] Request New Ticket\n  [2] Pay for Exisiting Parking Ticket\nEnter your choice here: ')
        if user_input == '1':
            park.takeTicket()
        elif user_input== '2':
            park.payForParking()
            park.leaveGarage()
        else:
            print('You have made an invalid selection.  Please try again using [1] or [2]')


    # print(park.tickets)
    # print(park.parkingSpaces)
    # print(park.currentTicket)



runner()