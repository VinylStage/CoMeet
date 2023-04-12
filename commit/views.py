from django.shortcuts import render, redirect
from .models import Commit
# Create your views here.


def home(request):
    """
    기본메인페이지. 남는 사람이 하는걸로 !
    """
    user = request.user.is_authenticated
    if user:
        return redirect('/main')
    else:
        return redirect('/sign-in')

def commit(request):
    if request.method == 'GET':
        # user = request.user.is_authenticated
        # if user:
            # commit 모델에 저장한 모든 데이터를 불러옴
        all_commit = Commit.objects.all().order_by('-created_at')
        return render(request, 'commit/main.html', {'commit':all_commit})
        # else:
        #     return redirect('/sign-in')


def detail(request):
    """
    상세 게시글. 발전 시키게 된다면 댓글 기능까지! -윤보영-
    detail/1 detail/2
    """

# 로그인 확인은 홈 화면에서 글쓰기 버튼 눌러올 때 if 사용해서 로그인 상태 확인하면 될듯합니다!
def write_view(request):
    """
    게시글 쓰기. 백지현
    """
    if request.method == 'GET':
        """
        화면 띄워주기
        """
        return render(request, 'commit/write_view.html')
    
        
    if request.method == 'POST':
        """
        데이터베이스에 값 저장
        """
        user = request.user
        my_commit = Commit()
        my_commit.author = user
        my_commit.header = request.POST.get('my-header','')
        my_commit.content = request.POST.get('my-content','')
        my_commit.save()
        return redirect('/')
        


def edit_view(request):
    """
    게시글 수정 임상빈
    """


def delete_view(request):
    """
    게시글 삭제. 남는 사람이 하는걸로 !
    """
