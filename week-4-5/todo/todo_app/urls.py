from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path("", views.list_todo, name="list"),
    path("create/", views.create, name="create_form"),
    path("create-todo/", views.create_todo, name="create_todo"),
    path("delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),
    path("edit/<int:todo_id>/", views.edit, name="edit_form"),
    path("update/<int:todo_id>/", views.update_todo, name="update_todo"),
    #django forms
    path("dfcreate/",views.todo_form,name="django_list"),
    path("dfindex/",views.dfindex,name="dfindex"),
    path("dfindex/todos/", views.get_todos, name="get_todos"),
    path("dfindex/delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),
]
