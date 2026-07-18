from models.project import Project
from models.task import Task
from models.user import User


def test_create_project():
    project = Project(
        "CLI Tool",
        "Course Project",
        "2026-08-20"
    )

    assert project.title == "CLI Tool"
    assert project.tasks == []
    assert project.contributors == []


def test_add_task():
    project = Project(
        "CLI Tool",
        "Course Project",
        "2026-08-20"
    )

    task = Task("Build CLI")

    project.add_task(task)

    assert len(project.tasks) == 1
    assert project.tasks[0].title == "Build CLI"


def test_add_contributor():
    project = Project(
        "CLI Tool",
        "Course Project",
        "2026-08-20"
    )

    user = User("Alex", "alex@gmail.com")

    project.add_contributor(user)

    assert len(project.contributors) == 1
    assert project.contributors[0].name == "Alex"


def test_complete_task():
    project = Project(
        "CLI Tool",
        "Course Project",
        "2026-08-20"
    )

    task = Task("Create CLI")

    project.add_task(task)

    project.complete_task("Create CLI")

    assert task.status == "Completed"