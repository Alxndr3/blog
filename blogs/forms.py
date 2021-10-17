from django import forms
from .models import BlogPost


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['text']
        labels = {'text': ''}

        def __str__(self):
            """Return a string represetation of teh model."""
            return self.text

