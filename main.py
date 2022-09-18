# landing feature that will ask user what they wish to do within the app - Add a new meber, check for fines, check overdues, and check for available services.
from dataclasses import dataclass


def landing():
    input("Hello, what would you like to do first? Create a new member? Check for fines, check overdues or check for available services")
    for input in features:
    else:
     return "we do not have that feature apologies"


#list of functions that landing page can loop through and execute
features = (create_new_member, fine_check, overdues, check_for_available_services)


# feature 1 Library worker inputs information here for new members to the library 

class Library_member():
    def __init__(self, name, date_of_birth, fines,)   
        self.self = self
        self.name = name
        self.date_of_birth = date_of_birth
        self.fines = fines

#list to store new members
new_members = [
     Library_member ("Kane", 26 3 1993, 0 ),
     Library_member ("Chantal", 11 7 1994, 0),
     Library_member ("Jack", 22 11 2003, 0),
]
def create_new_member(): 
        name = input("Please enter the name of the new member")
        if input != ""
         print ("Invalid input: Please enter the name of the new member")
 else:
    x

 date_of_birth = input("Please enter the date of birth of the new member in the format YYYY-MM-DD")
      if input != int()
        print ("Invalid input: Please enter the DOB of the new member as numbers in the format YYYY-MM -DD. For example the 26th of March 1993 would be represented as 26-03-1993")
      else:
         x

   
    fines = input(int("please enter any fine amounts as a number. If patron has no fines then enter 0"))
        if input != int()
            print ("Invalid input: Please enter an number between 1-14")
        else: 
            x

    x = Library_member.new_members.append(name, date_of_birth, fine)





# Feature 2 allows users to check for library fines
# How will we be able to check for other members
# cannot be a for loop
def fine_check():
    for fine in new_member1:
      if fine in new_member1 = 0 ?????????
         print ("you do not have any fines")
    else: 
        print (f"you have a fine of {fine}")







# Feature 3 allows users to check how many days they have left until renewal or return
def overdue():
        user_input = user_input(int("how many days have you had the item? please enter a number between 1 and 14"))
        if user_user input is not inte 
        print ("please put in the days represent as numbers such as one = 1") # this needs a rework
        result = user_input(int) - 14
        return (f"you have {result} days left of this item")








#Feature 4 this allows users to check what services are available and if they are free, bookable or cost

services available {
    "scanning" = "free",
    "printing" = "costs per page",
    "borrowing" = "free",
    "study room" = "bookable",
    "computers" = "bookable",
    "librarian" = "bookable",
    "local history" = "free",

}

for items in services available 
    check for user_user input ("Hi there what service are you looking for? Please input the name of the service otherwise input finished")
    if input in service avaible 
    print (f" We have this {key} service and it is {value}")
    else: 
        print (" Apologise we do not have that service. Would you like to search for more?")
    if user_input is "end" 
    return ("Thank you please come again")

    