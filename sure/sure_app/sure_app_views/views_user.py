from django.shortcuts import render, redirect
from ..forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render

# User model 커스터마이징시 
from django.contrib.auth import get_user_model
User = get_user_model()


#회원가입 renewal by 준경
from django.contrib import messages

def register(request):
    error_message = ''
    success_message = ''  # 추가: 회원가입 성공 메시지 변수

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        username = request.POST.get('username')
        
        if User.objects.filter(username=username).exists():
            error_message = "이미 존재하는 아이디입니다."
        elif form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            if password1 == password2:
                user = User.objects.create_user(username=username, password=password1)
                user = authenticate(request, username=username, password=password1)
                
                if user is not None:
                    login(request, user)
                    success_message="가입완료" # 회원가입 성공 메시지 설정
                    return redirect('main')
            else:
                form.add_error('password2', 'Passwords do not match')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form, 'error_message': error_message, 'success_message':success_message })




# 로그인
def login_Form(request):
    # 이미 로그인한 경우
    if request.user.is_authenticated:
        return redirect('main')
    
    else:
        form = LoginForm(data=request.POST or None)
        if request.method == "POST":

            # 입력정보가 유효한 경우 각 필드 정보 가져옴
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                # 위 정보로 사용자 인증(authenticate사용하여 superuser로 로그인 가능)
                user = authenticate(request, username=username, password=password)

                # 로그인이 성공한 경우
                if user is not None:
                    login(request, user) # 로그인 처리 및 세션에 사용자 정보 저장
                    return redirect('main')  # 리다이렉션
        return render(request, 'login.html', {'form': form}) #폼을 템플릿으로 전달

# 동네인증
@login_required
def location_auth(request):

    location = request.user.location
    return render(request, "location.html", {"location": location})

# 지역설정
@login_required
def set_location(request):
    if request.method == "POST":
        location = request.POST.get('region-setting')

        if location:
            try:
                user_tmp, created = User.objects.get_or_create(user=request.user)
                user_tmp.location = location
                user_tmp.save()

                return redirect('location')
            except Exception as e:
                return JsonResponse({"status": "error", "message": str(e)})
        else:
            return JsonResponse({"status": "error", "message": "Region cannot be empty"})
    else:
        return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)


# 지역인증 완료
@login_required
def set_location_certification(request):
    if request.method == "POST":
        request.user.profile.region_certification = 'Y'
        request.user.profile.save()
        messages.success(request, "인증되었습니다")
        return redirect('location')