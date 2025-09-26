#A register over students in a class
from colorama import Fore, Style

database = []



def add_student():
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
    for student in database:
        print(database)

def search():
    search_student = str(input("Enter name of student: "))
    found = False

    for student in database:
        if student["name"] == search_student:
            print(f"---Name: {student['name']}--Age: {student['age']}---")
            found = True

        else:
            print(Fore.RED+("No student with that name."))
            Fore.RESET

def avg_age():
    total = 0
    for val in database:
        total += val
        avg = total /len(val)
        print(f"Average student-age: {avg}")


def menu():

    menu_is_running = True
    while menu_is_running:
        print (Fore.GREEN + Style.BRIGHT+"***Main menu***\n",
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
                print("4")
                Fore.RESET
            elif choice == "5":
                print("Exiting program...bye!")
                break
        except ValueError:
            print("Try a valid number from 1-5")

menu()