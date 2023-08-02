from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone
from bcuser.models import Bcuser 

def post_list(request):
    # Post 데이터 베이스의 모든 데이터 가져오기(publiShed_date가 현재시간 기준 이전 시간꺼 모두 가져오기)
    # publiShed_date__lte: 여기서 lte는 "less than or equal to"의 약자로,
    # 이는 publiShed_date 필드 값이 지정된 값보다 작거나 같은 객체를 필터링하겠다는 의미.
    posts=Post.objects.filter(publiShed_date__lte=timezone.now()).order_by('-publiShed_date')
    return render(request,'blog/post_list.html', {'posts':posts})

def post_new(request):
    if request.method == 'POST':
        # POST 데이터와 함께 제출된 파일을 사용하여 PostForm 인스턴스를 생성
        form=PostForm(request.POST, request.FILES) # 입력정보 받아오기
        if form.is_valid(): 
            post=form.save(commit=False)
            # 게시글의 작성자를 현재 로그인한 사용자로 설정
            # request.user : 로그인 했을 때 django에서 만들어주는 객체
            user_id= request.session.get('user')
            bcuser= Bcuser.objects.get(pk=user_id) # asign 할당 문제와 코드흐름
            
            post.author = bcuser
            #게시글의 게시일자를 현재 시간으로 설정
            post.publiShed_date = timezone.now()
            post.save()
            return redirect('post_list') # post 후 목록확인
    else:
        form=PostForm()
    return render(request, 'blog/post_new.html', {'form':form})

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk) # Post : models의 Post 데이터베이스
    return render(request, 'blog/post_detail.html', {'post':post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        # POST 데이터와 함께 제출된 파일을 사용하여 PostForm 인스턴스를 생성
        form = PostForm(request.POST, request.FILES, instance=post) # 입력정보 받아오기
        if form.is_valid(): 
            post=form.save(commit=False)
            
            user_id= request.session.get('user')
            bcuser= Bcuser.objects.get(pk=user_id) # asign 할당 문제와 코드흐름
            post.author = bcuser
            
            post.publiShed_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk) # post 후 목록확인
    else:
        # 편집할 post 인스턴스를 사용하여 PostForm
        form=PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})


def post_delete(request, pk): 
    # 로그인한 계정(bcuser의 models에 write의 정보)
    user_id = request.session.get('user')
    bcuser= Bcuser.objects.get(pk=user_id)
    
    # 예외처리
    if not request.session.get('user'):
            return redirect('post_detail')

    # # 게시글 번호 가져오기
    # board = Board.objects.get(pk=pk) #유저 정보 관련된 객체만 집어옴

    if Bcuser.objects.get(pk=user_id) == post.author:
        board.delete()
    else:
        raise Http404("권한이 없습니다. ")
    return redirect('post_list')