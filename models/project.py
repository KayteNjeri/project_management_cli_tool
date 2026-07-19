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

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": []
        }

    def __repr__(self):
        return self.title
    
    