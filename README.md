---------------------------------------------------------------------------
---Student-register---
----------------------------------------------------------------------------

A tiny console app for managing a class roster. Add students, list them, search by name, and compute the average age — all from a simple menu.

Features

Add student (name, age, hobby)

List all students

Search a student by exact name

Calculate and print average age

Colored output via colorama

In-memory storage (no files/DB)

---------------------------------------------------------------------------
---Requirements---
----------------------------------------------------------------------------

Python 3.9+

colorama

pip install colorama

Run
python app.py

---------------------------------------------------------------------------
---Usage---
----------------------------------------------------------------------------

On start you’ll see a menu:

***Main menu***
1. Add student
2. List all students
3. Search student
4. Calculate average student-age
5. Exit program


Enter a number (1–5) to perform an action. Prompts will guide you (e.g., name, age, hobby). Output uses color for clarity.
---------------------------------------------------------------------------
---Notes---
----------------------------------------------------------------------------

Data is stored only in memory; restarting the app resets the register.

Input validation prints helpful error messages on invalid types.

Example
Choose a number from 1-5 in the menu:
1
Enter name: Alice
Enter age: 17
Enter a favorite hobby: Piano
Student added to database...

2
---Name: Alice--Hobby: Piano---

4
Average student-age: 17.0 years.

License

Copyright © 2025 Mallard-Dash. All rights reserved.
