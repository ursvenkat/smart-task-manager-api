# Smart Task Manager API

A RESTful task management system designed for teams and organizations to efficiently manage work items, track progress, assign tasks, and generate productivity reports.

## Features

### User Management
- User Registration
- User Login
- JWT Authentication
- Role Based Access Control

### Task Management
- Create Task
- Update Task
- Delete Task
- Task Assignment
- Priority Management
- Status Tracking

### Reporting
- Active Tasks
- Completed Tasks
- User Productivity Report

## Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite
- JWT Authentication
- Pytest

## Project Structure

smart-task-manager-api/
│
├── app.py
├── config.py
├── database.py
├── models.py
├── requirements.txt
│
├── routes/
│ ├── auth.py
│ ├── users.py
│ └── tasks.py
│
├── tests/
│ ├── test_auth.py
│ ├── test_tasks.py
│ └── test_users.py
│
└── docs/
└── API_Documentation.md

## Future Enhancements

- Docker Deployment
- Email Notifications
- AWS Deployment
- Team Collaboration
- Kanban Board

## Author

Venkatesh Patte
