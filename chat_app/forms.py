from django import forms
from .models import ChatMessage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ChatMessageForm(forms.ModelForm):
    message = forms.CharField(label='Сообщение', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ChatMessage
        fields = ['message']
