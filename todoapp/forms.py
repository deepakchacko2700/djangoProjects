from . models import Task
from django import forms

class ToDoForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['priority', 'date']