from django import forms
from django.core import validators
from . import models

class BbForm(forms.ModelForm):
    price = forms.FloatField(validators=[validators.MinValueValidator(0.0, message='Введите число больше 0')])
    class Meta:
        model = models.Bb
        fields = ['title', 'content', 'price', 'rubric', 'img']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('text',)