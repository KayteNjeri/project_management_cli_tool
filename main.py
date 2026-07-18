#!/usr/bin/env python3
import argparse

from rich import print
from utils.storage import load_data, save_data

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

#add user commands
add_user = subparsers.add_parser("add-user")

add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)

args = parser.parse_args()
data = load_data()

if args.command == "add-user":

    data["users"].append({
        "name": args.name,
        "email": args.email,
        "projects": []
    })

    save_data(data)

    print(f"[green]User {args.name} created[/green]")

# Add Projects
add_project = subparsers.add_parser("add-project")
add_project.add_argument("--user", required=True)
add_project.add_argument("--title", required=True)
add_project.add_argument("--description", required=True)
add_project.add_argument("--due-date", required=True)

#Add Tasks
add_task = subparsers.add_parser("add-task")
add_task.add_argument("--project", required=True)
add_task.add_argument("--title", required=True)

#Complete tasks
complete = subparsers.add_parser("complete-task")
complete.add_argument("--project", required=True)
complete.add_argument("--title", required=True)

# List Projects
list_projects = subparsers.add_parser("list-projects")
list_projects.add_argument("--user", required=True)
