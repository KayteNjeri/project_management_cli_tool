from models.person import Person

class User(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
        self.projects = []

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("An invalid email")
        self._email = value

    def add_a_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "projects": [project.to_dict()
            for project in self.projects]
        }
    
    @classmethod
    def from_dict(cls, data):
        from models.project import Project

        user = cls(
            data["name"],
            data["email"]
        )

        for project_data in data.get("projects", []):
            user.add_a_project(
                Project.from_dict(project_data)
            )

        return user

    def __repr__(self):
        return f"{self.name} ({self.email})"
    
   