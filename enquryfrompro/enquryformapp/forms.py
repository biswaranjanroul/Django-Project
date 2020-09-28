from django import forms
from multiselectfield import MultiSelectFormField
class EnquryForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name:",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Yours Name'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email:",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Yours Email'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Mobile Number:",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Yours Mobile Number'
            }
        )
    )
    COURSES_CHOICES = (
        ('PY', 'Python'),
        ('DJ', 'Django'),
        ('RA', 'Rest API')
    )
    course=MultiSelectFormField(choices=COURSES_CHOICES,label="Select your required courses")
    LOCATION_CHOICES = (
        ('HYD', 'Hyderbad'),
        ('BANG', 'Bangalore'),
        ('che', 'Chennai')
    )
    location=MultiSelectFormField(choices=LOCATION_CHOICES,label="select your required location")
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female')
    )
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect,label="Select your Gender")
    start_date=forms.DateField(
        widget=forms.SelectDateWidget(),
        label="select your date:"
    )