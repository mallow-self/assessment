# Todo - Instructions
1. Create a conda venv here:
    - `conda create -n todo_env python=3.12`
2. Activate it
3. Initialize poetry for the project:
    - `poetry init`
4. Add django:
    - `poetry add django`
5. Create a django project
    - `django-admin startproject todo`
6. Go into todo:
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
    - `python3 manage.py runserver`

---
## Notes:
1. create a app inside the django project
2. Add it in settings
3. Set up initial app,urls,views,settings
4. Make and migrate
5. create a todo table model and migrate
6. create a super user
    ```
        > python3 manage.py createsuperuser
        Username (leave blank to use 'rishicollinz'): admin
        Email address: admin@gmail.com
        Password: 123
        Password (again): 123
        This password is too short. It must contain at least 8 characters.
        This password is too common.
        This password is entirely numeric.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.
    ```
7. changed timezone
8. Added template,table,css and js for the list page
9. Done read,delete,create,update
10. css adding
11. 