from models.task import Task
from models.user import User

def test_create_task():

    task = Task("Design Database")

    assert task.title == "Design Database"
    assert task.status == "Pending"
    assert task.assigned_to is None

def test_complete_task():

    task = Task("Create CLI")

    task.complete()

    assert task.status == "Completed"

def test_assign_user():
    task = Task("Design Models")

    user = User("Alex", "alex@gmail.com")

    task.assign(user)

    assert task.assigned_to == user

def test_task_repr():

    task = Task("Create CLI")

    assert repr(task) == "Create CLI (Pending)"