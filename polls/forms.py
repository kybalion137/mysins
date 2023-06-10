from django import forms


class UserForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=20, widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(min_value=10, max_value=100, widget=forms.NumberInput(attrs={"class": "myfield"}))
    goal = forms.CharField(min_length=3, max_length=30, widget=forms.TextInput(attrs={"class": "myfield"}))
    work = forms.CharField(min_length=3, max_length=30, widget=forms.TextInput(attrs={"class": "myfield"}))
    tg = forms.URLField(widget=forms.TextInput(attrs={"class": "myfield"}))
