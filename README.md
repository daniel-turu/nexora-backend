# Django Project Setup Guide

## Introduction
This guide will walk you through setting up and running the Django project on your local machine.

## Prerequisites
Before installing, ensure you have the following installed on your system:
- Python (>= 3.12)
- pip (Python package manager)
- virtualenv (create virtual environment)

## Installation Steps

https://github.com/daniel-turu/nexora-backend.git

### 2. Create and Activate a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 5. Create a Superuser (Optional, for Admin Access)
```sh
python manage.py createsuperuser
```
Follow the prompts to set up a username and password.

### 6. Run the Development Server
```sh
python manage.py runserver
```

Access the project at:
```
http://127.0.0.1:8000/
```



## Environment Variables
If your project requires environment variables, create a `.env` file and configure them accordingly.


- Collect static files (for production):
  ```sh
  python manage.py collectstatic
  ```

## Deployment
For deployment instructions, follow the guidelines for your hosting provider (e.g., Heroku, AWS, DigitalOcean, etc.).


---

Happy Coding! 🚀