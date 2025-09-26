#A register over students in a class
#Copyright Mallard-Dash 2025
from colorama import Fore, Style
import time

database = [] #This is where all students are stored



def add_student(): #Function for adding students in database
    try:
        name = str(input("Enter name: "))
    except ValueError:
        print(Fore.RED+("Plese enter only letters"))
        Fore.RESET
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print(Fore.RED+("Please enter only integers"))
        Fore.RESET
    try:
        hobby = str(input("Enter a favorite hobby: "))
    except ValueError:
        print(Fore.RED+("Plese enter only letters"))
        Fore.RESET
    add = {
        "name":name,
        "age":age,
        "hobby": hobby
    }
    database.append(add)

def show():
    for student in database: #Function that shows the user all students in the database
        print(f"---Name: {student['name']}--Hobby: {student['hobby']}---")

def search():
    try:
        search_student = str(input("Enter name of student: ")) #Search for a specific student by name
    except ValueError:
        print(f"Enter a valid student name:")

    for student in database:
        if student["name"] == search_student:
            print(f"---Name: {student['name']}--Hobby: {student['hobby']}---")
            return

        else:
            print(Fore.RED+("No student with that name."))
            Fore.RESET

def avg_age():
    total_age = 0 #Calculate the average age of the students
    if len(database) == 0:
        print(f"There is no students in the database")
              
    for student in database:
        total_age += student['age']
        avg = total_age /len(database)
        print(f"Average student-age: {avg} years.")
        


def menu():

    menu_is_running = True
    while menu_is_running:
        print (Fore.GREEN +"***Main menu***\n",
            f"1. Add student\n",
            f"2. List all students\n",
            f"3. Search student\n",
            f"4. Calculate average student-age\n",
            f"5. Exit program")
        try :
            choice = input("Choose a number from 1-5 in the menu: \n")
            if choice == "1":
                add_student()
                print("Student added to database...")
                Fore.RESET
            elif choice == "2":
                show()
                Fore.RESET
            elif choice == "3":
                search()
                Fore.RESET
            elif choice == "4":
                avg_age()
                Fore.RESET
            elif choice == "5":
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(1)
                print(Fore.CYAN + "Exiting program...")
                break
        except ValueError:
            print("Try a valid number from 1-5")

menu()