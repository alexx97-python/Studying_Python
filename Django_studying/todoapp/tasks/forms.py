from django.forms import ModelForm, CharField, TextInput
from .models import Task


class TasksForm(ModelForm):
    title = CharField(widget=TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Task
        fields = ('title', 'progress', 'completed')
