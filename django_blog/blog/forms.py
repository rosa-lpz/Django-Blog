from django import forms
from .models import Category, Topic, Post


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': ''}


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'text']
        labels = {'name': 'Name', 'text': 'Text'}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
        labels = {'title': 'Post Title', 'text':'Text'}
        # widget 80 columns
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

 