# Todo API Backend

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/django-4.0+-green.svg)
![DRF](https://img.shields.io/badge/djangorestframework-3.14+-red.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A RESTful API backend for a Todo application with JWT authentication, built with Django and Django REST Framework.

## Features

- **JWT Authentication** (Access/Refresh tokens)
- **CRUD Operations** for Todos
- **User-specific Data** (Users only see their own todos)
- **Filtering/Search** (by status, priority)
- **Validation** for all inputs
- **Swagger/OpenAPI** documentation

## Tech Stack

- **Python 3.9+**
- **Django 4.0+**
- **Django REST Framework**
- **SimpleJWT** for authentication
- **PostgreSQL** (or SQLite for development)

## Prerequisites

- Python 3.9+
- PostgreSQL (or SQLite)
- pipenv/pip

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AshrafJB2/TodoFlow.git
   cd TodoFlow
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```
   don't forget to setup environment variables
   