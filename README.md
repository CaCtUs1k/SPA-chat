# SPA-chat
# Windows/MacOS install

1. If you are using PyCharm - it may propose you to automatically create venv for your project 
    and install requirements in it, but if not:

    `python -m venv venv`

    `venv\Scripts\activate` (on Windows)

    `source venv/bin/activate` (on macOS)

    `pip install -r requirements.txt`
2. Then use following commands:

    `python manage.py makemigrations`

    `python manage.py migrate`
3. Configure .env flie
   
4. Use following command:

   `python manage.py runserver`

# Docker install
    
    docker pull cactus717/django-chat

    docker run -p 8000:8000 cactus717/django-chat

Then go to http://localhost:8000