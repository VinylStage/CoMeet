from django.shortcuts import render, redirect
import time
from .models import Commit, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def home(request):
    return redirect('/detail')


def detail(request):
    if request.method == 'GET':
        all_commit = Commit.objects.all().order_by('-created_at') # order_by : tweet이 생성된 시간 순으로 출력 해줌(하지만 안에 '-'를 넣어줌으로써 역순으로 정렬된다.)
        return render(request, 'main.html', {'commit_':all_commit})
        
    elif request.method == 'POST':
        users = request.user
        all_commit = Commit()
        all_commit.writer = users
        all_commit.content = request.POST.get('my-content', '')
        all_commit.save()
        return redirect('/detail')


def detail_commit(request, id):
    my_commit = Commit.objects.get(id=id)
    commit_comment = Comment.objects.filter(commit_id=id).order_by('-created_at')
    return render(request, 'detailpage.html', {'my_commit_':my_commit, 'comment':commit_comment})


def detail_write_comment(request, id):
    user = request.user.is_authenticated
    if user:
        if request.method == 'POST':
            comment = request.POST.get("comment","")
            current_commit = Commit.objects.get(id=id)

            TC = Comment()
            TC.comment = comment
            TC.writer = request.user
            TC.commit = current_commit
            TC.save()
            return redirect('/detail/'+str(id))
    else:
        messages.warning(request, '댓글 작성을 위해서는 로그인이 필요합니다')
        return redirect('/detail/'+str(id))

@login_required
def detail_delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    current_commit = comment.commit.id
    comment.delete()
    return redirect('/detail/'+str(current_commit))

def write_view(request):
    """
    게시글 쓰기. 백지현
    """


def edit_view(request, pk):
    """
    게시글 수정 임상빈
    """


def delete_view(request):
    """
    게시글 삭제. 남는 사람이 하는걸로 !
    """
