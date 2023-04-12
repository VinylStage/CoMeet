from django.shortcuts import render, redirect
# login_required : 로그인이 되어있어야만 실행되게 하는 함수
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from .models import User


def log_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        # 암호화 된 비밀번호와 현재 비밀번호가 일치하는지 확인하는 함수
        me = auth.authenticate(request, username=username, password=password)
        # 사용자가 db안에 있으면(비어있지 않으면)
        if me is not None:
            # 장고가 알아서 로그인 시켜줌
            auth.login(request, me)
            print('로그인 성공')
            return redirect('/')
        else:
            return redirect('/log_in')
        
    elif request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            return redirect('/')
        else:
            return render(request, 'user/login.html')

@csrf_exempt
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')
            else:
                User.objects.create_user(username=username, password=password, email=email)
                return redirect('/log_in')


@login_required
def log_out_view(request):
    auth.logout(request)
    return redirect('/')


@login_required
def my_page_view(request):
    """
    마이페이지, 내 프로필 수정, (비밀번호 초기화)
    엘리사님
    """
