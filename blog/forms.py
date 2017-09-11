from django import forms

from .models import Post, Content

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
		
class ContentForm(forms.ModelForm):

    class Meta:
        model = Content
        fields = ('content',)