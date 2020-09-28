from django import forms
class Empform(forms.Form):
    name=forms.CharField(max_length=100)
    location=forms.CharField(max_length=100)
    salary=forms.IntegerField()
    email=forms.EmailField(max_length=100)
    name=forms.CharField(
        label="Enter your Name:",
        widget=forms.TextInput

    )
    name=forms.CharField(
        label="Enter your Name:",
        widget=forms.TextInput
    )
