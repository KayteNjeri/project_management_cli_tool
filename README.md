# 📋 A Command-Line Interface (CLI) Project Management Tool

A Python-based Command-Line Interface (CLI) application that enables administrators to manage users, projects, and tasks through CLI commands. .

---

## ✨ Features

- Create and manage users
- Add projects to specific users
- View all registered users
- View projects assigned to a user
- Add tasks to projects
- Mark tasks as completed
- Persist data using file I/O
- Display formatted CLI output using Rich
- Unit tests using Pytest

---

## 📁 Project Structure

```text
project_management_cli_tool/
│
├── data/
│   └── database.json
│
├── models/
│   ├── person.py
│   ├── project.py
│   ├── task.py
│   └── user.py
│
├── tests/
│   ├── test_project.py
│   ├── test_storage.py
│   ├── test_task.py
│   └── test_user.py
│
├── utils/
│   └── storage.py
│
├── main.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── requirements.txt
```

---

## 🛠️ Technologies Used

- Python 3
- argparse
- JSON
- Rich
- Pytest

---

## 🏗️ Object-Oriented Design

The application follows Object-Oriented Programming principles.

### 📦 Classes

- Person
- User
- Project
- Task

### 🔗 Relationships

```text
Person
   │
   ▼
 User
   │
   ├── Project
   │      ├── Task
   │      ├── Task
   │      └── Task
   │
   └── Project
```

### 💡 OOP Concepts Implemented

- Inheritance (`Person → User`)
- Encapsulation using `@property`
- Class attributes (`id_counter`)
- Class methods (`from_dict()`)
- Instance methods
- Object composition
- Object serialization using `to_dict()`

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/KayteNjeri/project_management_cli_tool
```

Navigate into the project

```bash
cd project_management_cli_tool
```

Create a virtual environment (optional)

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Display help

```bash
python main.py --help
```

---

## 💻 CLI Commands

### 👤 Add a User

```bash
python main.py add-user --name "Alex" --email "alex@gmail.com"
```

Example output

```
User 'Alex' added successfully.
```

---

### 👤 Test Duplicate Users

```bash
python main.py add-user --name "Alex" --email "alex@gmail.com"
```

---

### 📋 List Users

```bash
python main.py list-users
```

---

### 📁 Add a Project

```bash
python main.py add-project --user alex@gmail.com --title "CLI Tool" --description "Project Tracker" --due-date "2026-08-15"
```

---

### 📂 List Projects

```bash
python main.py list-projects --user alex@gmail.com
```

---

### ✅ Add a Task

```bash
python main.py add-task --project "CLI Tool" --title "Build CLI"
```

---

### ✔️ Complete a Task

```bash
python main.py complete-task \
--project "CLI Tool" \
--title "Create CLI"
```

---

## 💾 Data Persistence

Application data is stored locally in

```
data/database.json
```

The project uses JSON serialization through:

- `load_data()`
- `save_data()`

The application also handles:

- Missing files
- Invalid JSON data

using exception handling.

---

## 📦 External Packages

### 🌟 Rich

The Rich package is used to improve the appearance of command-line output by displaying formatted tables and coloured messages.

Install manually if needed.

```bash
pip install rich
```

---

## 🧪 Testing

This project uses **Pytest** for unit testing.

Run all tests

```bash
pytest
```

Run a single test file

```bash
pytest tests/test_user.py
```

Current test coverage includes:

- User model
- Project model
- Task model
- Storage utilities

---

## 🏛️ Design Decisions

This project follows a modular architecture by separating responsibilities into different folders.

- `models/` contains the application classes.
- `utils/` contains reusable helper functions.
- `data/` stores persistent JSON data.
- `tests/` contains unit tests.
- `main.py` serves as the CLI entry point.

The application uses `argparse` to implement a multi-command interface and follows Python best practices, including:

- `if __name__ == "__main__":`
- Object-Oriented Programming
- JSON persistence
- Exception handling
- Modular code organization

---

## 🚀 Future Improvements

Possible enhancements include:

- Delete users, projects, and tasks
- Search tasks by status
- Due date validation
- Task priorities
- User authentication
- Export project reports

---

## 👩‍💻 Author

This project has been built as part of a Python assessment project to demonstrate backend development concepts and practices.

---

## 📄 License

This project is licensed under the MIT License.