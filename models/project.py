from models.task import Task

class Project:
    id_counter = 1

    def __init__(self, title, description, due_date):
        self.id = Project.id_counter
        Project.id_counter += 1

        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def add_a_task(self, task):
        self.tasks.append(task)

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return True
        return False

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [task.to_dict() 
                      for task in self.tasks]
        }
    
    @classmethod
    def from_dict(cls, data):

        project = cls(
            data["title"],
            data["description"],
            data["due_date"]
        )

        for task_data in data.get("tasks", []):
            project.add_a_task(
                Task.from_dict(task_data)
            )

        return project

    def __repr__(self):
        return self.title
    
    