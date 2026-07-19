#!/usr/bin/env python3
import argparse

from rich import print
from rich.table import Table

from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data

def main():
    parser = argparse.ArgumentParser(
        description="Project Management CLI"
)

    subparsers = parser.add_subparsers(dest="command")

# Add a user
    add_user = subparsers.add_parser("add-user")

    add_user.add_argument("--name", required=True)
    add_user.add_argument("--email", required=True)

# List Users
    subparsers.add_parser("list-users")

# Add Projects
    add_project = subparsers.add_parser("add-project")

    add_project.add_argument("--user", required=True)
    add_project.add_argument("--title", required=True)
    add_project.add_argument("--description", required=True)
    add_project.add_argument("--due-date", required=True)

# List Projects
    list_projects = subparsers.add_parser("list-projects")

    list_projects.add_argument("--user", required=True)

# Add Tasks
    add_task = subparsers.add_parser("add-task")

    add_task.add_argument("--project", required=True)
    add_task.add_argument("--title", required=True)
    add_task.add_argument("--assigned-to", default="")

# Complete tasks
    complete = subparsers.add_parser("complete-task")

    complete.add_argument("--project", required=True)
    complete.add_argument("--title", required=True)

    args = parser.parse_args()
    data = load_data()

# Add User Logic
    if args.command == "add-user":

        for user in data["users"]:
            if user["email"] == args.email:
                print("[red]User already exists.[/red]")
                return

        user = User.from_dict({
            "name": args.name,
            "email": args.email,
            "projects": []
        })

        data["users"].append(user.to_dict())

        save_data(data)

        print(f"[green]User '{user.name}' added successfully.[/green]")

# List users logic
    elif args.command == "list-users":

        table = Table(title="Users")

        table.add_column("Name")
        table.add_column("Email")

        for user in data["users"]:
            table.add_row(user["name"], user["email"])

        print(table)

#Add Project Logic
    elif args.command == "add-project":

        found = False

        for user in data["users"]:
            if user["email"] == args.user:
                project = Project.from_dict({
                    "title": args.title,
                    "description": args.description,
                    "due_date": args.due_date,
                    "tasks": []
                })

                user["projects"].append(project.to_dict())

                save_data(data)

                print(f"[green]Project '{args.title}' added.[/green]")

                found = True
                break

        if not found:
            print("[red]User not found.[/red]")

# List projects logic
    elif args.command == "list-projects":

        found = False

        for user in data["users"]:
            if user["email"] == args.user:
                table = Table(title=f"Projects for {user['name']}")

                table.add_column("Title")
                table.add_column("Description")
                table.add_column("Due Date")

                for project in user["projects"]:
                    table.add_row(
                        project["title"],
                        project["description"],
                        project["due_date"])

                print(table)

                found = True
                break

        if not found:
            print("[red]User not found.[/red]")
    
# Add a task logic
    elif args.command == "add-task":

        found = False

        for user in data["users"]:
            for project in user["projects"]:
                if project["title"] == args.project:
                    task = Task.from_dict({
                        "title": args.title,
                        "status": "Pending",
                        "assigned_to": args.assigned_to
                    })

                    project["tasks"].append(task.to_dict())

                    save_data(data)

                    print("[green]Task added successfully.[/green]")

                    found = True
                    break

        if not found:
            print("[red]Project not found.[/red]")

#Complete task logic
    elif args.command == "complete-task":

        found = False

        for user in data["users"]:
            for project in user["projects"]:
                if project["title"] == args.project:
                    for task in project["tasks"]:
                        if task["title"] == args.title:
                            task["status"] = "Completed"

                            save_data(data)

                            print("[green]Task completed.[/green]")

                            found = True
                            break

        if not found:
            print("[red]Task not found.[/red]")
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()