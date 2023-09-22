from django import forms

# 로그인 
class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder' : 'Username', 'class':'login-input'}),
        label='',
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder' : 'Password', 'class':'login-input'}),
        label='',
    )