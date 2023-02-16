from django import forms
from .models import Todo_item
import datetime
class TodoForm(forms.ModelForm):
    class Meta:
        model =Todo_item 
        fields = ['title','content','is_done']
class updateform(forms.ModelForm):
    class Meta:
        model=Todo_item
        fields=['title','content','is_done']
        exclude = ('created_at',)


    