from django import forms
from core.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            # Binds the native HTML5 calendar/time selector dropdown
            "deadline": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control"
                },
                format="%Y-%m-%dT%H:%M"
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Sets a clean placeholder description for your tasks
        self.fields["content"].widget.attrs.update({
            "placeholder": "What needs to be done?",
            "rows": 3
        })
        # Uses a Bootstrap-friendly multiple-select layout for tags
        self.fields["tags"].widget.attrs.update({
            "class": "form-select"
        })
