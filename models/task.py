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

    def assign(self, user):
        self.assigned_to = user

    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to.name 
            if self.assigned_to else None
        }
    
    @classmethod
    def from_dict(cls, data):

        task = cls(
            data["title"],
            data.get("assigned_to")
        )

        task.status = data["status"]

        return task

    def __repr__(self):
        return f"{self.title} ({self.status})"
    
    