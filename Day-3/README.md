# Day 3 - Student Grade Manager

## What the program does

The Student Grade Manager is a menu-driven Python program for managing student information and subject marks.

The program allows the user to:

* Add a student with multiple subjects and marks
* Search for a student using their ID
* Sort students alphabetically by name
* Calculate the average marks of a student
* Display all student data
* Generate an average marks report for all students
* Validate student IDs, subject names, marks, and other inputs

The program also uses a **dictionary comprehension** to generate the average marks report.

## How to Run

Open the `Day-3` folder in the terminal and run:

```bash
python student_grade_manager.py
```

## Sample Run

```text
1. Add student
2. Search student
3. Sort students
4. Average Marks
5. Display
6. Report
7. Exit

Enter your choice: 1
Enter student ID: S101
Enter student name: Ananya
Enter number of subjects: 3
Enter subject name: Python
Enter marks of the subject: 85
Enter subject name: SQL
Enter marks of the subject: 90
Enter subject name: Django
Enter marks of the subject: 80

Student added successfully...

Enter your choice: 6
Student ID: S101    Average Marks: 85.0
```

## Average Marks Report

The report is generated using dictionary comprehension:

```python
report = {stud_id: avg_marks(stud_id) for stud_id in students}
```

This creates a dictionary containing each student ID and their corresponding average marks.

## Concepts Used

* Dictionaries
* Nested dictionaries
* Functions
* Function parameters and return values
* `if` / `elif` / `else`
* `while` and `for` loops
* `sorted()` with `lambda`
* Dictionary comprehension
* Input validation
* `try` / `except`
* String methods such as `strip()` and `title()`
* Basic calculations

## Testing

Run the tests using:

```bash
pytest -v
```