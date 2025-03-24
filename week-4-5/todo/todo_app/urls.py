from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path("", views.index, name="dfindex"),
    path("update/<int:todo_id>/", views.update_todo, name="update_todo"),
    path("todos/", views.get_todos, name="get_todos"),
    path("delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),
    path("get_todo_update/<int:todo_id>/",views.get_todo_update, name="get_todo_update")
]
