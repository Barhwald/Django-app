# from turtle import title
from django import forms

class PostForm(forms.Form):
    title = forms.CharField(initial='Post title')
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":1, "cols":30}))
    image = forms.FileField()