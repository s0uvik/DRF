### Tech Stack

- Django Rest Framework
- Django
- Python Request
- Django Cors Headers

### Commands

- python -m venv venv
- source venv/Scripts/activate
- pip freeze
- pip install -r requirements.txt
- pip install --upgrade pip
- django admin startproject cfehome
- python manage.py runserver
- python manage.py startapp [app name]
- python manage.py makemigrations
- python manage.py migrate
- python manage.py shell

### how you add data using shell

from products.models import Products

> > > Products.objects.create(title= "Mouse", content="mouse description", price=12.00)
