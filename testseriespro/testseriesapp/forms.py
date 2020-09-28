from django import forms


class SignupForm(forms.Form):
    first_name = forms.CharField(
        label="Enter Your First Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }
        )
    )
    last_name = forms.CharField(
        label="Enter Your Last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )

    username = forms.CharField(
        label="Enter Your User Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'User Name'
            }
        )
    )


class loginForm(forms.Form):
    username = forms.CharField(
        label="Enter Your User Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'User Name'
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )
class logoutForm(forms.Form):
    username = forms.CharField(
        label="Logout",
        widget=forms.PasswordInput(
           attrs={
                'class': 'form-control',

           }
        )
    )

