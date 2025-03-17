from django.contrib import admin
from .models import Todo


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["todo_id","title","priority_level","due_date","status","updated_at"]