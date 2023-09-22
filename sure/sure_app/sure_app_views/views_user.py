from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ..forms import LoginForm

def register(request):
    return render(request, 'register.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('dangun_app:main')
    
    else:
        form = LoginForm(data=request.POST or None)
        if request.method == "POST":

            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('dangun_app:main')  # 로그인시 메인
        return render(request, 'login.html', {'form': form})
    
def location(request):
    return render(request, 'location.html')
