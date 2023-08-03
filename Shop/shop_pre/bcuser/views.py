from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
from .models import Bcuser


def index(request):
    return render(request, 'index.html', {'email':request.session.get('user')})

# FormView : Get 또는 POST 요청을 처리해주는 비즈니스 로직 라이브러리
class RegisterView(FormView):
    template_name='register.html' # 사용할 템플릿 이름
    form_class = RegisterForm # 참고할 forms.py에 있는 클래스 즉 폼 클래스
    success_url='/login/' # RegisterForm이 성공적으로 처리된 후 redirect될 url 지정
    
    def form_valid(self, form):
        bcuser=Bcuser(
            email=form.data.get('email'),
            password = make_password(form.data.get('password')),
            level='user'
        )
        
        #User의 email객체들 중 form에 입력한 email과 같은 대상이 존재하면,
        if Bcuser.objects.filter(email=form.data.get('email')).exists():
            form.add_error('email', '이미 사용 중인 이메일 입니다.')
            return self.form_invalid(form)
        else:
            bcuser.save()
            
        return super().form_valid(form)
    
class LoginView(FormView):
    template_name='login.html' # 사용할 템플릿 이름
    form_class = LoginForm # 참고할 forms.py에 있는 클래스 즉 폼 클래스
    success_url='/' # RegisterForm이 성공적으로 처리된 후 redirect될 url 지정

    def form_valid(self, form):
        
        
        self.request.session['user']=form.data.get('email')
        return super().form_valid(form)
    
    
def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')