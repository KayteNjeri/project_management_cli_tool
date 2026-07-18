import pytest
from models.user import User
from models.project import Project


def test_create_user():
    user = User("Alex", "alex@gmail.com")

    assert user.name == "Alex"
    assert user.email == "alex@gmail.com"
    assert user.projects == []


def test_add_project():
    user = User("Alex", "alex@gmail.com")
    project = Project("CLI Tool", "Tracker", "2026-08-20")

    user.add_project(project)

    assert len(user.projects) == 1
    assert user.projects[0].title == "CLI Tool"


def test_invalid_email():
    with pytest.raises(ValueError):
        User("Alex", "alexgmail.com")


def test_remove_project():
    user = User("Alex", "alex@gmail.com")
    project = Project("CLI Tool", "Tracker", "2026-08-20")

    user.add_project(project)
    user.remove_project("CLI Tool")

    assert len(user.projects) == 0