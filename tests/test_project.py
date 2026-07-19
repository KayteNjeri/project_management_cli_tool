from models.project import Project
from models.task import Task
from models.user import User


def test_create_project():
    project = Project(
        "CLI Tool",
        "Project Tracker",
        "2026-08-20")

    assert project.title == "CLI Tool"
    assert project.description == "Project Tracker"
    assert project.due_date == "2026-08-20"
    assert project.tasks == []
    
def test_add_task():
    project = Project(
        "CLI Tool",
        "Tracker",
        "2026-08-20")

    task = Task("Create CLI")

    project.add_a_task(task)

    assert len(project.tasks) == 1
    assert project.tasks[0].title == "Create CLI"

def test_complete_task():
    project = Project(
        "CLI Tool",
        "Tracker",
        "2026-08-20"
    )

    task = Task("Create CLI")

    project.add_task(task)

    project.complete_task("Create CLI")

    assert task.status == "Completed"