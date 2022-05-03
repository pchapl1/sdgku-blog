from django.forms import ModelForm
from django import forms

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title':forms.TextInput(attrs={'class' : 'form-control' }),
            'body' : forms.Textarea(attrs={'class' : 'form-control' }),
            'author' : forms.Select(attrs={'class' : 'form-control form-select' }),
        }