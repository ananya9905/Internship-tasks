students = {}

def add_stud(stud_id, name, subjects):
    if stud_id in students:
        return "ID already exist!!!"
    else:
        students[stud_id] = {"Name": name, "Subjects": subjects}
        return "Student added successfully..."

def search_stud(search_id):
    if search_id in students:
        return f"Student ID: {search_id}\nStudent Name: {students[search_id]['Name']}\nSubjects: {students[search_id]['Subjects']}"
    else:
        return "Student not found!!!"
    
def sort_stud():
    sorted_ids = sorted(students, key = lambda stud_id: students[stud_id]["Name"].lower())
    return sorted_ids

def avg_marks(stud_id):
    subjects = students[stud_id]["Subjects"]
    if not subjects:
        return None
    average = sum(subjects.values()) / len(subjects)
    return round(average, 2)

def avg_report():
    report = {stud_id: avg_marks(stud_id) for stud_id in students}
    return report
        
def show():
    return students

def get_int(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
        except ValueError:
            pass
        print(f"Please enter a number between {low} and {high}")
        
def get_unique_value(prompt, existing_values, error_msg):
    while True:
        value = input(prompt).strip().title()
        if not value:
            print("Value cannot be empty!!!")
            continue
        if value in existing_values:
            print(error_msg)
        else:
            return value 
        
def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Value cannot be empty!!!")
            continue
        break
    return value
        
def main():
    while True:
        print("1. Add student\n2. Search student\n3. Sort students\n4. Average Marks\n5. Display\n6. Report\n7. Exit")
        user = get_int("Enter your choice: ", 1, 7)
        
        if user == 1:
            stud_id = get_unique_value("Enter student ID: ", students, "Student ID already exist...")
            name = get_non_empty("Enter student name: ")
            num = get_int("Enter number of subjects: ", 1, 10)
            subjects = {}
            for _ in range(num):
                subject = get_unique_value("Enter subject name: ", subjects, "Subject already exist...")
                mark = get_int("Enter marks of the subject: ", 0, 100)
                subjects[subject] = mark
            print(add_stud(stud_id, name, subjects))
        
        elif user == 2:
            search_id = input("Enter Id to search: ").strip()
            print(search_stud(search_id))
        
        elif user == 3:
            sorted_ids = sort_stud()
            for stud_id in sorted_ids:
                print(f"Student ID: {stud_id}\nStudent Name: {students[stud_id]['Name']}")
        
        elif user == 4:
            sid = input("Enter student ID: ").strip()
            if sid not in students:
                print("ID does not exist!!!")
            else:
                average = avg_marks(sid)
                if average is None:
                    print("No subjects available. Cannot calculate average!!!")
                else:
                    print(f"Average marks: {average}")
        
        elif user == 5:
            print(show())
            
        elif user == 6:
            report = avg_report()
            for stud_id, average in report.items():
                print(f"Student ID: {stud_id}\tAverage Marks: {average}")
        
        elif user == 7:
            break
            
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye")