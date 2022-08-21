class ParkingGarage():
    def __init__(self, capacity):
        self.tickets = []
        self.parkingSpaces = []
        self.currentTicket = {}
        self.capacity = capacity

# Robert Coded the welcome method
    def welcome(self):
        print("\n+++++ +++++ +++++ +++++ Welcome To The Parking Garage +++++ +++++ +++++ +++++\n")
        print("Please select from the following options:")

# Julian Coded the takeTicket method
    def takeTicket(self):
        print("\n+++++ +++++ +++++ +++++ Get Parking Ticket +++++ +++++ +++++ +++++\n")
        if self.parkingSpaces == []:
            print("I'm sorry, there are no parking spaces avaliable at this time. Please come back soon.")
        else:
            print("Thank you for requesting a ticket.")
            print(f"You have ticket number {self.tickets[0]}. Have a Great Day!")
            del(self.tickets[0])
            del(self.parkingSpaces[0])
            print(f"There are {len(self.parkingSpaces)} parking spaces remaining.")
        

# Robert Coded the payForParking method
    def payForParking(self):
        print("\n+++++ +++++ +++++ +++++ Pay For Parking +++++ +++++ +++++ +++++\n")
        paymentTicketNumber = input("To pay for parking please enter your ticket number: ")
        if paymentTicketNumber.isnumeric() == False:
            print("You have entered your ticket number incorrectly.  Please try again.")
            self.payForParking()
        elif int(paymentTicketNumber) in self.currentTicket.keys(): 
            paymentAmount = input("Your current balance is $10 for parking.  Please enter payment amount here: $")
            if paymentAmount.isnumeric() == True:
                if int(paymentAmount) == 10:
                    print("Thank you for payment of $10.  Your ticket has been paid and you have 15 minutes to leave the garage.")
                    self.currentTicket[int(paymentTicketNumber)] = True
                    self.leaveGarage()
                elif int(paymentAmount) < 10:
                    print(f"Your payment total is insufficient by ${10 - int(paymentAmount)}.  Please pay $10.")
                    self.payForParking()
                elif int(paymentAmount) > 10:
                    print(f"Your payment total is too much by ${int(paymentAmount) - 10}.  Please pay $10.")
                    self.payForParking()
            elif paymentAmount.isnumeric() == False:
                print("\nWe request you only use numbers for payment. Please try again.")
                self.payForParking()
        elif int(paymentTicketNumber) not in self.currentTicket.keys():
            print("Your ticket number is invalid.  Please try again.")
            self.payForParking()
            
# Julian Coded the leaveGarage method
    def leaveGarage(self):
        print("\n+++++ +++++ +++++ +++++ Exit Parking Garage +++++ +++++ +++++ +++++\n")
        ticket_num = input("To exit the Garage, please share your ticket number: ")
        if int(ticket_num) in self.currentTicket.keys():
            if ticket_num.isnumeric() == True:
                for key,value in self.currentTicket.items():
                    if key == int(ticket_num) and value == True:
                        print(f"Thank you for parking with us, Have a wonderful Day!") 
                        self.tickets.append(ticket_num)
                        self.parkingSpaces.append(ticket_num)
                    elif key == int(ticket_num) and value == False:
                        print("You have entered your ticket number incorrectly.  Please try again.")
                        self.leaveGarage()
            elif ticket_num.isnumeric() == False:
                print("You have entered your ticket number incorrectly.  Please try again.")
                self.leaveGarage()
        elif int(ticket_num) not in self.currentTicket.keys():
            print("Your ticket number is invalid.  Please try again.")
            self.leaveGarage()
                

park = ParkingGarage(5)

# Robert coded the runner function
def runner():
    for ticket in range(1, park.capacity + 1):
        park.tickets.append(ticket)
        park.parkingSpaces.append(ticket)
        park.currentTicket[int(ticket)] = False
    while True:
        park.welcome()
        user_input = input(f'  [1] Request New Ticket\n  [2] Pay for Exisiting Parking Ticket\nEnter your choice here: ')
        if user_input == '1':
            park.takeTicket()
        elif user_input== '2':
            park.payForParking()
            for key, value in park.currentTicket.items():
                park.currentTicket[key] = False
        else:
            print('\nYou have made an invalid selection.  Please try again using [1] or [2]')

runner()
