from django.shortcuts import render, redirect
from django.http import Http404
from .models import Board
from .forms import BoardForm
from bcuser.models import Bcuser
from tag.models import Tag
from django.core.paginator import Paginator

# Create your views here.


def board_list(request):
    all_boards = Board.objects.all().order_by("-id")
    page = int(request.GET.get("p", 1))  # 초기에 페이지는 1로 시작
    paginator = Paginator(all_boards, 3)  # 전체 글을 가져와서 5개씩 나누어 보여줌

    boards = paginator.get_page(page)
    return render(request, "board_list.html", {"boards": boards})


def board_write(request):
    # 세션영역에 id가 존재하지 않으면 로그인 하고 오도록 login.html페이지로 넘긴
    if not request.session.get("user"):
        return redirect("/bcuser/login/")
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():  # 폼의 데이터가 유효한 정보인지 여부
            user_id = request.session.get("user")  # 세션에서 로그인한 아이디 확보
            bcuser = Bcuser.objects.get(pk=user_id)  # 실제 데이터 베이스에서 로그인한 id 가져오기

            tags = form.cleaned_data["tags"].split(",")

            board = Board()  # 게시판의 객체 생성 : 유효성 검사가 통과된 데이터를 저장하기 위함
            board.title = form.cleaned_data["title"]
            board.contents = form.cleaned_data["contents"]
            board.write = bcuser  # 로그인한 id 데이터베이스에 저장
            board.save()

            for tag in tags:
                if not tag:  # 태그가 없을면 통과
                    continue
                # _tag, _ : 등록되어 있는 태그와 새로 생성한 태그 저장
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)  # 태그에 저장

            return redirect("/board/list/")
    else:
        form = BoardForm()  # 접속은 했으나 유효성 검사를 안했으므로 다시 유효성 검사부터 진행
    # 실패시 처음으로 돌아가 => 다시 해봐
    return render(request, "board_write.html", {"form": form})


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404("게시글을 찾을 수 없습니다.")

    return render(request, "board_detail.html", {"board": board})


def board_update(request, pk):
    # 로그인 정보
    user_id = request.session.get('user')

    if not request.session.get("user"):
        return redirect("/bcuser/login/")

    try:
        # 게시글 정보
        board = Board.objects.get(pk=pk) 
    except Board.DoesNotExist:
        raise Http404("게시글을 찾을수 없습니다.")
    
    # models의 참조조건이 설정되어 있으므로 값이 일치해야함
    if Bcuser.objects.get(pk=user_id) == board.writer:

        if request.method == "POST":
            form = BoardForm(request.POST)
            if form.is_valid():  # 폼의 데이터가 유효한 정보인지 여부
                user_id = request.session.get("user")  # 세션에서 로그인한 아이디 확보
                bcuser = Bcuser.objects.get(pk=user_id)  # 실제 데이터 베이스에서 로그인한 id 가져오기

                board.title = form.cleaned_data["title"]
                board.contents = form.cleaned_data["contents"]
                board.write = bcuser  # 글의 작성자
                board.save()
                return redirect("/board/list/")
        else:
            form = BoardForm(initial={"title": board.title, "contents": board.contents})   
    else:
        raise Http404("권한이 없습니다.")
    
    return render(request, "board_update.html", {"form": form})

def board_delete(request, pk):
    # 로그인한 계정(bcuser의 models에 write의 정보)
    user_id = request.session.get('user')

    # 예외처리
    if not request.session.get('user'):
        return redirect('/bcuser/login/')
    
    # 게시글 번호 가져오기
    board=Board.objects.get(pk=pk)

    if Bcuser.objects.get(pk=user_id) == board.writer:
        board.delete()
    else:
        raise Http404("권한이 없습니다. ")
    
    return redirect('board_list')

