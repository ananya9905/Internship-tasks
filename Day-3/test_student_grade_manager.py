import pytest
from student_grade_manager import students, add_stud, search_stud, sort_stud, avg_marks, avg_report, show, get_int, get_unique_value, get_non_empty

@pytest.fixture(autouse = True)
def clear_stud():
    students.clear()
    
def test_duplicate_stud_id():
    add_stud("BE101", "Ananya", {"Math": 80})
    result = add_stud("BE101", "Rahul", {"Python": 90})
    assert result == "ID already exist!!!"
    assert students["BE101"]["Name"] == "Ananya"
    
def test_avg_marks():
    add_stud("BE101", "Ananya", {"Python": 90, "Maths": 75, "SQL": 80})
    assert avg_marks("BE101") == 81.67
    
def test_sort_stud():
    add_stud("BE101", "Rahul", {"Python": 80})
    add_stud("BE102", "Ananya", {"Python": 90})
    add_stud("BE103", "Priya", {"Python": 70})
    result = sort_stud()
    assert result == ["BE102", "BE103", "BE101"]
    
def test_duplicate_subject(monkeypatch):
    subjects = {"Math": 80}
    inputs = iter(["math", "Physics"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = get_unique_value("Enter subject name: ", subjects, "Subject already exist...")
    assert result == "Physics"