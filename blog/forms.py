from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'categories']
        labels = {
            'title': 'Título',  # Tradução do campo 'title'
            'slug': 'URL amigável',  # Tradução do campo 'slug'
            'content': 'Conteúdo',  # Tradução do campo 'content'
            'categories': 'Categorias',  # Tradução do campo 'categories'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'}),

        }
        



