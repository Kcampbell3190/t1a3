# landing feature that will ask user what they wish to do within the app - Add a new meber, check for fines, check overdues, and check for available services.
from dataclasses import dataclass
# how do data types work in in loops etc
#list of functions that landing page can loop through and execute
features = ("create_new_member", "fine_check", "overdues", "check_for_available_services")
choice = ""

# feature 1 Library worker inputs information here for new members to the library 

class LibraryMember():
    def __init__(self, name, date_of_birth, fines,):
        self.self = self
        self.name = name
        self.date_of_birth = date_of_birth #into a date type
        self.fines = fines

#list to store new members
new_members = [
     LibraryMember("Kane", 26_3_1993, 0 ),
     LibraryMember("Chantal", 11_7_1994, 0),
     LibraryMember("Jack", 22_11_2003, 0),



def landing():
    while True:
        print("1) Create a new member")
        print("2) Check for fines")
        print("3) Check overdues")
        print("3) Check for available services")
        choice = input("Please select a number from the menu: ")
        choice = choice.strip()


    if (choice == "1"):
        def create_new_member(): 
            name = input("Please enter the name of the new member")
        if input != "string":
         print ("Invalid input: Please enter the name of the new member")
        else:
           

        date_of_birth = print("Please enter the date of birth of the new member in the format YYYY-MM-DD")
        x == input
        if x != int():
          print ("Invalid input: Please enter the DOB of the new member as numbers in the format YYYY-MM -DD. For                    example the 26th of March 1993 would be represented as26-03-1993")
        else:
          x




# Feature 2 allows users to check for library fines
        # How will we be able to check for other members
        # cannot be a for loop
    if (choice == "2"):
        
    def fine_check():
        print("What is the member number?")
          x = input
    for fine in x:
      if fine in x == 0
         print("you do not have any fines")
    else: 
        print(f"you have a fine of {fine}")
       

# Feature 3 allows users to check how many days they have left until renewal or return
    if (choice == "3"):
        def overdue():
            x = int(input("how many days have you had the item? please enter a number between 1 and 14"))
        if isinstance(x, int):
            print ("please put in the days represent as numbers such as one = 1") # this needs a rework
            result = (x - 14)
            return (f"you have {result} days left of this item")



#Feature 4 this allows users to check what services are available and if they are free, bookable or cost
    if (choice == "4"):
        services_available {
    "scanning": "free",
    "printing": "costs per page",
    "borrowing": "free",
    "study room": "bookable",
    "computers": "bookable",
    "librarian": "bookable",
    "local history": "free",
}

    for items in services_available:
        print("Hi there what service are you looking for? Please input the name of the service otherwise input finished")
        x = input
    if input in service_avaible 
        print (f"We have this {key} service and it is {value}")
    else: 
        print (" Apologise we do not have that service. Would you like to search for more?")
    if x is "finished"
      print("Thank you please come again")
