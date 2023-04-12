from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
# login_required : 로그인이 되어있어야만 실행되게 하는 함수
from django.contrib.auth.decorators import login_required



def log_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password) # my_user에 있는 암호화된 비밀번호와 현재 입력된 비밀번호가 일치하는지, 그것이 사용자와 맞는지까지 알려줌
        if me is not None:
            auth.login(request, me)
            return redirect('/detail')
        else:
            return redirect('/log_in')
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/detail')
        else:
            return render(request, 'user/login.html')

def sign_up_view(request):
    if request.method == 'GET': # GET 메서드로 요청이 들어 올 경우
        user = request.user.is_authenticated
        if user:
            return redirect('/detail')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST': # POST 메서드로 요청이 들어 올 경우
        username = request.POST.get('username', None) 
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user: # == True:
                print("중복된 이름입니다. 다시 작성해주세요.")
                return render(request, 'user/signup.html')
            else:
                User.objects.create_user(username=username, password=password)
                return redirect('/log_in')


@login_required
def log_out_view(request):
    auth.logout(request)
    return redirect('/log_in')

@login_required
def my_page_view(request):
    """
    마이페이지, 내 프로필 수정, (비밀번호 초기화)
    엘리사님
    """
