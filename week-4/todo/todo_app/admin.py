from django.contrib import admin
from .models import Todo


# Todo model is registered in admin site
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["todo_id","title","priority_level","due_date","status","updated_at"]