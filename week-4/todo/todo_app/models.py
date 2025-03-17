from django.db import models


# Create your models here.
class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]

    todo_id = models.AutoField(primary_key=True)  # Primary key auto increments
    title = models.TextField()
    priority_level = models.CharField(max_length=10, choices=PRIORITY_CHOICES) # a field with dropdown(high,medium,low)
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)  # a field with dropdown(pending,in-progress,completed,overdue)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation - only added once not updated
    updated_at = models.DateTimeField(auto_now=True) # updated after every edit
