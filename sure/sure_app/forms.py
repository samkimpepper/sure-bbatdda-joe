from django import forms
from .models import Goods

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


# 회원가입
class RegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '아이디를 입력해주세요', 'class': 'login-input'}),
        label='아이디',
        label_suffix='', 
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요', 'class': 'login-input'}),
        label='비밀번호',
        label_suffix='', 
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 다시 입력해주세요', 'class': 'login-input'}),
        label='비밀번호 확인',
        label_suffix='', 
    )

# 게시물
class GoodsForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)  
    location = forms.CharField(max_length=100)

    class Meta:
        model = Goods
        fields = ['title', 'description', 'price', 'location', 'img']
