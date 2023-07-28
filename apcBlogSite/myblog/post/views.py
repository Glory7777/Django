from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    posts=Post.objects.all()
    return render(request,'post_list.html', {'posts':posts})

def post_detail(request, pk):
    # 해당 댓글을 찾지 못하면 서버는 404 에러를 반환
    post=get_object_or_404(Post, pk=pk) # Post : models의 Post 데이터베이스
    comments=post.comments.all()
    
    if request.method == 'POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            # commit=False : DB에 즉시 저장하지 말고 객체를 반환하여 수정을 허용
            comment.post=post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form=CommentForm()
        
    return render(request, 'post_detail.html',{'post':post, 'comments':comments,'comment_form':comment_form})
        
def post_new(request):
    pass