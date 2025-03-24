from django import forms
from django.core.exceptions import ValidationError
from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Task title'}),
        label="Title",
        required=False
    )
    priority_level = forms.ChoiceField(
        choices=Todo.PRIORITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Priority",
        required=False
    )
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label="Date",
        required=False
    )
    status = forms.ChoiceField(
        choices=Todo.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Status",
        required=False 
    )

    class Meta:
        model = Todo
        fields = ("title", "priority_level", "due_date", "status")

    def clean_priority_level(self):
        data = self.cleaned_data.get("priority_level")
        if data == "":
            raise ValidationError("Priority level is required.")
        return data

    def clean_status(self):
        data = self.cleaned_data.get("status")
        if data == "":
            raise ValidationError("Status is required.")
        return data
    
    def clean_title(self):
        data = self.cleaned_data.get("title")
        if data == "":
            raise ValidationError("Title is required.")
        return data
    
    def clean_due_date(self):
        data = self.cleaned_data.get("due_date")
        if data == None:
            raise ValidationError("Due-Date is required.")
        return data
