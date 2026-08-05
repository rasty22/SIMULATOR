# Django Project Setup

## 1. Create Project Folder
```bash
mkdir serial
cd serial
```

## 2. Create Virtual Environment
```bash
python3 -m venv venv
```

## 3. Activate Virtual Environment

### macOS/Linux
```bash
source venv/bin/activate
```

### Windows
```cmd
venv\Scripts\activate
```

## 4. Install Django
```bash
pip install django
```

## 5. Create Django Project
```bash
django-admin startproject serial .
```

## 6. Apply Initial Migrations
```bash
python manage.py migrate
```

## 7. Create Superuser
```bash
python manage.py createsuperuser
```

## 8. Create an App
```bash
python manage.py startapp accounts
```

Add the app to `INSTALLED_APPS` in `settings.py`.

## 9. Create and Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## 10. Run the Development Server
```bash
python manage.py runserver
```

Open in your browser:

- Home: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

---

# Daily Commands

Activate virtual environment:

```bash
source venv/bin/activate
```

Run the server:

```bash
python manage.py runserver
```

After changing models:

```bash
python manage.py makemigrations
python manage.py migrate
```

Deactivate the virtual environment:

```bash
deactivate
```

HTTP method:
GET: FETCHED DATA
POST: CREATE
PUT: FULL UPDATE
PATCH: PARTIAL UPDATE
DELETE: DELETE
