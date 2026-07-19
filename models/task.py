class Task:
    id_counter = 1

    def __init__(self, title, assigned_to=None):
        self.id = Task.id_counter
        Task.id_counter += 1

        self.title = title
        self.status = "Pending"
        self.assigned_to = assigned_to

    def complete(self):
        self.status = "Completed"

    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    def __repr__(self):
        return f"{self.title} ({self.status})"
    
    