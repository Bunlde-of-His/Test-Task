from django import forms
from .models import User, Group


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'group']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['group'].widget.attrs.update({'class': 'form-control'})


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Description'})
