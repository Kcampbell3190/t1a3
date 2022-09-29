
import datetime  

features = ("create_new_member", "fine_check", "overdues", "check_for_available_services")


 #Functions####################################################################
 
def create_new_member(): 
        name = input("Please enter the name of the new member: ")
        if name.isnumeric():
            print ("Invalid input: Please enter the name of the new member")
            name = input("Please enter the name of the new member: ")
        else:
            day = int(input("Please enter the day of birth of the new member: ")) #rework to readable
            month = int(input("please enter the month of birth of the new member: "))
            year = int(input("Please enter the year of birth of the new member: "))
            birthday = datetime.date(year, month, day) 
        print("All done!")
        new_members.append(LibraryMember(name, birthday))

       
     

def overdue():
        num = int(input("how many days have you had the item? please enter a number between 1 and 14: "))
        if num <= 14:
            result = (14 - num)
            print (f"you have {result} days left of this item")
        else: 
            print ("your item is overdue please return or renew the item")
        
            
       





    #for items in services_available:
def services_available():
 servicelist = {
        "scanning": "free",
    "printing": "costs per page",
    "borrowing": "free",
    "study room": "bookable",
    "computers": "bookable",
    "librarian": "bookable",
    "local history": "free",
}
 service = input("Hi there what service are you looking for?: ")
        
 if service in servicelist:
        print (f"We have this {service} service and it is {servicelist[service]}")
 if service not in servicelist:
        print (" Apologise we do not have that service. Would you like to search for more?")
if input == "finished":
      print("Thank you please come again")

            #############################################################################################################
             
            
class LibraryMember():
    def __init__(self, name, birthday):
        self.self = self
        self.name = name
        self.birthday = birthday 
        

#list to store new members or do I want it stored in different variables 

new_members = [
    
     LibraryMember("Chantal", "11 7 1994"),
     LibraryMember("Jack", "22 11 2003"), 
]

# landing feature that will ask user what they wish to do within the app - Add a new meber, check for fines, check overdues, and check for available services.

def landing():
    try:
        print("1) Create a new member")
        print("2) Check overdues")
        print("3) Check for available services")
        print("4) Exit ")
        choice = int(input("Please enter a number from the menu:"))
        if choice == 1:
         create_new_member()
        if choice == 2:
         overdue()
        if choice == 3:
         services_available()
        if choice == 4:
         print("Thank you please come again")
         quit()

        if choice not in range (1,5):
            print("please enter a number between 1 and 4")
            raise ValueError 
    except:
            return landing()

landing()