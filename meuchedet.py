# Please create a meuchedet patient(client).
# This patient will need a t.z, first name, last name, age, coverage plan (basic, adif, c), phone number
# This patient will also require different methods:
# Will need to have an increase of age every year,
# Will need to have a name update incase last name changes after marriage
# Will need to be charged money every month depending on age bracket and coverage plan
# Will need a call back method so that if the patient needs to be reached you can call their phone

# You will also need to think of one more attribute and method for the meuchedet patient

# After wards try thinking about ways of linking patients together - for example, maybe one patient has multiple patients under the same phone number, btu different t.z, maybe t.z should be an array?

# Use the __eq__ method to check if a t.z. already exists, then another patient with the same t.z cannot be added

# Use the __str__ method to print info about a patient

import datetime as dt
import coverage
from coverage import basic, adif, c

class Meuchedet:
    tdz=[]
    def __init__(self):
     
        self.tz = int(input("what is your tz?"))
        self.firstName = None
        self.lastName = None
        self.age = None
        self.coveragePlan = None
        self.phoneNumber = None
        self.gender = None
        # self.firstName = input ("What is your first name?")
        # self.lastName = input ("What is your last name?")
        # self.age = int(input("What is your age?"))
        # self.coveragePlan = input("What plan would you like, c, adif, or basic?")
        # self.phoneNumber = input("What is your phone number?")
        self.__class__.tdz.append(self.tz)

    def initClient(self):
        self.tz
        self.firstName = input ("What is your first name?")
        self.lastName = input ("What is your last name?")
        self.age = int(input("What is your age?"))
        self.coveragePlan = input("What plan would you like, c, adif, or basic?")
        self.phoneNumber = input("What is your phone number?")
        self.gender = input("What is your gender?")

    def update_age(self):
        birthdate = input("What is your day and month of birth? Must be entered in mm-dd format.")
        if dt.datetime.today().strftime("%m-%d") == birthdate:
            self.age = self.age + 1
 
        
    def update_lastname(self):
        quest = input("Do you have a new lastname? Please enter yes or no.")
        if quest == "yes" or quest =="YES" or quest == "Yes":
            newName = input("What is your new last name?")
            self.lastName = newName

    def charge(self):
        cost = 0
        if self.age <= 18 :
            cost = 20
        elif 18 < self.age <=50:
            cost = 40
        elif self.age >50:
            cost = 60
        if self.coveragePlan == 'c':
            cost += 20
        elif self.coveragePlan =='adif':
            cost += 10
        print (f"The cost of your plan {self.coveragePlan} at age {self.age} is {cost}")
   
    def call_number(self):
        quest = input("Do you need a patients phone number? Please enter yes or no.")
        if quest == "yes" or quest =="YES" or quest == "Yes":
            tz = int(input("Please enter patients tz number?"))
            if tz == self.tz:
                print(f"Patient {self.firstName} {self.lastName}, tz {self.tz} phone number is {self.phoneNumber}")
            else:
                print(f"There is no client with tz {tz}")
        else:
            pass

    #find out plan type according to gender.
    def gender_plan(self):
        print (f"The tz number {self.tz} has plan type '{self.coveragePlan}' and is gender type '{self.gender}'")
    
    def __eq__(self, other):
            if(self.tz == other.tz): 
                print (f"The tz {self.tz} already exists")

    @classmethod
    def new_tz(cls):
        Person2=Meuchedet()
        for each in cls.tdz:
            if Person2.tz != each:
                Person2.initClient()
            else:
                return Person1 == Person2
                #del Person2

            

    # I like this method better, but the assignmetn was to use the __eq__
    # @classmethod
    # def new_tz(cls):
    #     tzNew = int(input("please enter new patients tz"))
    #     for each in cls.tdz:
    #         if tzNew == each:
    #             print(f"That tz {tzNew} already exists in the system, pleae re-enter tz")
    #             tzNewTry = int(input("please enter new patients tz"))
    #             if tzNewTry == each:
    #                 print(f"That tz {tzNewTry} already exists in the system, pleae try again later")
    #         else:
    #             Person2 = Meuchedet()
            

    def __str__(self):
        return f"'tz: '{self.tz}, ', Firstname: '{self.firstName}, ', Lastname: ' {self.lastName}, ', Age: '{self.age}, ', Plan Type: '{self.coveragePlan}, ', Phone Number: ' {self.phoneNumber}, ', Gender: ' {self.gender}"


Person1 = Meuchedet()
Person1.initClient()
Person1.update_age()
Person1.update_lastname()
Person1.charge()
Person1.call_number()
Person1.gender_plan()
#Person2 = Meuchedet()
#Person2.initClient()
#print(Person1)
# Person2.update_age()
# print(Person1.age)
# Person2.update_lastname()
# print(Person1.lastName)
# Person2.charge()
# Person2.call_number()
# Person2.gender_plan()

Meuchedet.new_tz()


print(Person1)

