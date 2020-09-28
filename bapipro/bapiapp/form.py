from django import forms
class EmpForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    location = forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Location'
            }
        )
    )
    salary = forms.IntegerField(
        label="Enter Your Salary",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Salary'
            }
        )
    )
    email = forms.CharField(
        label="Enter Your Email",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }
        )
    )