from models.task import Task
from models.user import User


def test_create_task():
    task = Task("Implement argparse")

    assert task.title == "Implement argparse"
    assert task.status == "Pending"


def test_complete():
    task = Task("Write Tests")

    task.complete()

    assert task.status == "Completed"


def test_assign_user():
    task = Task("Design Models")

    user = User("Alex", "alex@gmail.com")

    task.assign(user)

    assert task.assigned_to == user