from django import forms

class EnquryForm(forms.Form):
    firstname = forms.CharField(
        label="Enter Your First Name:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }
        )
    )
    middlename = forms.CharField(
        label="Enter Your Middle Name:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'middle Name'
            }
        )
    )
    lastname = forms.CharField(
        label="Enter Your Last Name:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email Address:",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Phone Number:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }
        )
    )
    location = forms.CharField(
        label="Enter Your Current Location:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Current Location'
            }
        )
    )

    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female')
    )
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect,label="Select Your Gender")
