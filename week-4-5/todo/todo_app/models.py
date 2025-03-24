from django.db import models
from typing import List, Tuple
from datetime import date, datetime


# Create your models here.
class Todo(models.Model):
    """
    Represents a to-do item in the database.

    This model defines the structure for storing to-do tasks with attributes such as
    title, priority level, due date, status, and timestamps for creation and updates.

    Attributes:
        todo_id (AutoField): The primary key, auto-incremented for each to-do item.
        title (TextField): The title or description of the to-do task.
        priority_level (CharField): The priority level of the task (High, Medium, Low).
        due_date (DateField): The due date for completing the task.
        status (CharField): The current status of the task (Pending, In Progress, Completed, Overdue).
        created_at (DateTimeField): Timestamp when the task was created (auto-generated).
        updated_at (DateTimeField): Timestamp when the task was last updated (auto-updated).

    Choices:
        PRIORITY_CHOICES: Defines the available priority levels (High, Medium, Low).
        STATUS_CHOICES: Defines the available status options (Pending, In Progress, Completed, Overdue).
    """

    PRIORITY_CHOICES: List[Tuple[str, str]] = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]

    STATUS_CHOICES: List[Tuple[str, str]] = [
        ("pending", "Pending"),
        ("in-progress", "In Progress"),
        ("completed", "Completed"),
        ("overdue", "Overdue"),
    ]

    todo_id: int = models.AutoField(primary_key=True)  # Primary key auto increments
    title: str = models.TextField()
    priority_level: str = models.CharField(max_length=10, choices=PRIORITY_CHOICES)  # a field with dropdown(high,medium,low)
    due_date: date = models.DateField()
    status: str = models.CharField(max_length=15, choices=STATUS_CHOICES)  # a field with dropdown(pending,in-progress,completed,overdue)
    created_at: datetime = models.DateTimeField(auto_now_add=True)  # Timestamp for creation - only added once not updated
    updated_at: datetime = models.DateTimeField(auto_now=True)  # updated after every edit
