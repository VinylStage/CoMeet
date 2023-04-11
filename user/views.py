from django.shortcuts import render, redirect # login_required : 로그인이 되어있어야만 실행되게 하는 함수
from .models import UserModel        #태연
from django.http import HttpResponse  #태연
from django.contrib.auth import get_user_model  #태연
from django.contrib import auth     #태연
from django.contrib.auth.decorators import login_required       # 로그아웃 부분



def sign_up_view(request):      # 회원가입 부분 / 태연
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        # bio = request.POST.get('bio', None)

        if password != password2:    # 비밀번호 불일치시 회원가입 화면 다시 보여주기
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user :
                return render(request, 'user/signup.html')
            else:
                UserModel.objects.create_user(username=username, password=password)    #bio=bio 일단 빼놓기
                return redirect('/sign-in')



def sign_in_view(request):          # 로그인 부분 / 태연
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)


        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/sign-in/')
    
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')



# 로그아웃 부분  /  태연
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')






@login_required
def my_page_view(request):
    """
    마이페이지, 내 프로필 수정, (비밀번호 초기화)
    엘리사님
    """
