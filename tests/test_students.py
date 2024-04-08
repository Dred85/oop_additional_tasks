import pytest

from lesson1.students import Student


@pytest.fixture
def student():
    return Student("Алиса", "3 курс")


def test_init1(student):
    assert student.name == "Алиса"
    assert student.course == "3 курс"
