# landing feature that will ask user what they wish to do within the app - Add a new meber, check for fines, check overdues, and check for available services.

features = ("create_new_member", "fine_check", "overdues", "check_for_available_services")
choice = ""


 
 #Functions####################################################################
 
def create_new_member(): 
       #call class method
        name = input("Please enter the name of the new member: ")
        if name.isnumeric():
            print ("Invalid input: Please enter the name of the new member")
            name = input("Please enter the name of the new member: ")
        else:
          date_of_birth = input("Please enter the date of birth of the new member in the format YYYY-MM-DD")
          if date_of_birth.isstring():
            print("Invalid input: Please enter the DOB as a number")
            date_of_birth = input("Please enter the DOB of the new member")
          pass
          name = self.self
          name - name.self
          date_of_birth = self.date_of_birth
     

def overdue():
        num = int(input("how many days have you had the item? please enter a number between 1 and 14"))
        if num.isstring():
            print("Invalid input: Please enter a number between 1 and 14 as an integer")
        if num <= 14:
            result = (14 - num)
        print (f"you have {result} days left of this item")
        else: #num >= 14
        return ("your item is overdue please return or renew the item")
        
            
       





    #for items in services_available:
def services_available():
        
        serviceslist {
    "scanning": "free",
    "printing": "costs per page",
    "borrowing": "free",
    "study room": "bookable",
    "computers": "bookable",
    "librarian": "bookable",
    "local history": "free",
}

        print("Hi there what service are you looking for?")
        input = user_input("Enter the name of the service:")
    if input in servicelist
        print (f"We have this {key} service and it is {value}")
    else: 
        print (" Apologise we do not have that service. Would you like to search for more?")
    if input = "finished"
      print("Thank you please come again")

            #############################################################################################################
             
            
class LibraryMember():
    # def __init__(self, name, date_of_birth, fines,):
    def __init__(self, name, date_of_birth):
        self.self = self
        self.name = name
        self.date_of_birth = date_of_birth #into a date type
        # self.fines = fines
        self.fines = 0
    def check_fines():
        print(f"you have a fine of ${self.fines}")
 
        

         #print("you do not have any fines")
   # else: 
       # print(f"you have a fine of {fine}")

#list to store new members or do I want it stored in different variables 
kane = LibraryMember1("Kane", 26_3_1993, 10 )

new_members = [
     kane,
     LibraryMember("Chantal", 11_7_1994, 0),
     LibraryMember("Jack", 22_11_2003, 0),
]

# landing feature that will ask user what they wish to do within the app - Add a new meber, check for fines, check overdues, and check for available services.

def landing():
   # while True:
        print("1) Create a new member")
        print("2) Check for fines")
        print("3) Check overdues")
        print("4) Check for available services")
        print("5) Exit:")
        # choice = input("Please select a number from the menu: ")
       #  choice = choice.strip()

while user_input != '5':

    landing()
    choice = int(input("Enter your choice"))

   
 # feature 1 Library worker inputs information here for new members to the library  
    if (choice == 1):
        create_new_member()
       
      




# Feature 2 allows users to check for library fines
        # How will we be able to check for other members
        
    if (choice == "2"):
       fines() 
    
       

# Feature 3 allows users to check how many days they have left until renewal or return
    if (choice == "3"):
         overdue()
            



#Feature 4 this allows users to check what services are available and if they are free, bookable or cost
    if (choice == "4"):
        services_available()
    
    
    
    
    
    if (choice == "5"):
      print("Thank you please come again")
      break
