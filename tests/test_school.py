import pytest
from sources.school import Classroom, Teacher, Student, TooManyStudents
import allure


@allure.title("Test Authentication")
@allure.description("""This test attempts to log into the website using a login and a password. 
        Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.""")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_authentication():
    pass


@pytest.fixture
def empty_classroom():
    return Classroom(Teacher("Professor Snape"), [], "Potions")


@pytest.fixture
def full_classroom():
    students = [Student(f"Student{i}") for i in range(11)]
    return Classroom(Teacher("Professor McGonagall"), students, "Transfiguration")


@pytest.fixture
def harry():
    return Student("Harry Potter")


@pytest.fixture
def snape():
    return Teacher("Professor Snape")


def test_add_student(empty_classroom, harry):
    empty_classroom.add_student(harry)
    assert len(empty_classroom.students) == 1


def test_add_student_too_many_students(full_classroom, harry):
    with pytest.raises(TooManyStudents):
        full_classroom.add_student(harry)


def test_remove_student(full_classroom):
    student_name = full_classroom.students[1].name
    full_classroom.remove_student(student_name)
    assert len(full_classroom.students) == 10
    assert student_name not in [student.name for student in full_classroom.students]


def test_change_teacher(empty_classroom, snape):
    empty_classroom.change_teacher(snape)
    assert empty_classroom.teacher == snape
