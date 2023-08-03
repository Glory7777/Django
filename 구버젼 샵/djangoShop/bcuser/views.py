from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.views.generic.edit import FormView
from .forms import RegisterForm
from .models import Bcuser

def index(request):
    return render(request, 'index.html')

# FormView : Get 또는 POST 요청을 처리해주는 비즈니스 로직 라이브러리
class RegisterView(FormView):
    template_name='register.html' # 사용할 템플릿 이름
    form_class = RegisterForm # 참고할 forms.py에 있는 클래스 즉 폼 클래스
    success_url='/' # RegisterForm이 성공적으로 처리된 후 redirect될 url 지정
    
    def form_valid(self, form):
        bcuser=Bcuser(
            email=form.data.get('email'),
            password = make_password(form.data.get('password')),
            level='user'
        )
        bcuser.save()
        return super().form_valid(form)
