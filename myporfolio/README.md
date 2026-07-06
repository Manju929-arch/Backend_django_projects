# Portfolio

A complete Django portfolio website with authentication, dynamic projects, contact form, and modern responsive UI.

## Features

- User registration, login, logout, and password reset
- Dashboard with profile update and recent activity
- Projects fetched from Django models
- Contact form persists messages to SQLite
- Admin panel for managing users, projects, skills, certificates, resume, and messages
- Bootstrap 5 frontend, custom CSS, JS animations, and responsive design
- Static and media file handling

## Project Structure

- `accounts/` - authentication and profile management
- `portfolio/` - portfolio pages, models, and contact handling
- `templates/` - shared and app templates
- `static/` - CSS, JavaScript, and images
- `media/` - uploaded profile and project files
- `db.sqlite3` - default SQLite database

## Setup

1. Create and activate a Python virtual environment

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install Django

```powershell
pip install django
```

3. Run migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser

```powershell
python manage.py createsuperuser
```

5. Seed sample data

```powershell
python manage.py seed_portfolio
```

6. Run the development server

```powershell
python manage.py runserver
```

7. Open `http://127.0.0.1:8000/`

## Notes

- Password reset uses the console email backend for development
- Add real images and resume files under `static/images` and `media/`
- Configure `ALLOWED_HOSTS` and `DEBUG=False` for production
