from models.person import Person

class User(Person):
    def __init__(self, name, email:
        super().__init__(name)
        self.email = email
        self.projects = []

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@"  not in value:
            raise ValueError("An invalid email")
        self._email = value

    def add_a_project(self, project):
        self.projects.append(project)

    def __repr__(self):
        return f"{self.name} ({self.email})"
