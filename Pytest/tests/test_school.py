import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
par_dir = os.path.join(cur_dir, '..')
sys.path.insert(1, par_dir)

import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents



# Define fixtures for teacher, students, and classroom
@pytest.fixture
def harry_potter():
    return Teacher('Harry Potter')

@pytest.fixture
def hermione_granger():
    return Student('Hermione Granger')

@pytest.fixture
def ron_weasley():
    return Student('Ron Weasley')

@pytest.fixture
def hogwarts_classroom(harry_potter):
    students = []
    return Classroom(harry_potter, students, 'Defense Against the Dark Arts')



# Test cases for the Classroom class
def test_classroom_creation(hogwarts_classroom):
    assert hogwarts_classroom.teacher.name == 'Harry Potter'
    assert hogwarts_classroom.course_title == 'Defense Against the Dark Arts'
    assert len(hogwarts_classroom.students) == 0


def test_add_student(hogwarts_classroom, hermione_granger, ron_weasley):
    hogwarts_classroom.add_student(hermione_granger)
    hogwarts_classroom.add_student(ron_weasley)
    assert len(hogwarts_classroom.students) == 2


def test_add_too_many_student(hogwarts_classroom, hermione_granger):
    for _ in range(10):
        hogwarts_classroom.add_student(Student('Student'))
        
    with pytest.raises(TooManyStudents):
        hogwarts_classroom.add_student(hermione_granger)


def test_remove_student(hogwarts_classroom, hermione_granger, ron_weasley):
    hogwarts_classroom.add_student(hermione_granger)
    hogwarts_classroom.add_student(ron_weasley)
    
    hogwarts_classroom.remove_student('Hermione Granger')
    assert len(hogwarts_classroom.students) == 1
    assert hogwarts_classroom.students[0].name == 'Ron Weasley'


def test_change_teacher(hogwarts_classroom):
    new_teacher = Teacher('Severus Snape')
    hogwarts_classroom.change_teacher(new_teacher)
    assert hogwarts_classroom.teacher.name == 'Severus Snape'

