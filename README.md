# SPA-chat

SPA application for writing threads and lively discussions

https://django-chat-2jbp.onrender.com
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

# Demo

## Login
![Login](demo/login.png)

## Register
![Register](demo/register.png)

## Threads(main)
![Threads](demo/threads.png)

## Reply form
![Reply form](demo/reply_form.png)