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