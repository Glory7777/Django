from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Bcuser 
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm

# Create your views here.

# 껍데기 선언 후 요청받음

# 비즈니스 로직

def home(request):
    return render(request, 'home.html')
    # user_id=request.session.get('user')

    # if user_id: #user_id 가 있으면
    #     bcuser= Bcuser.objects.get(pk=user_id)
    #     return HttpResponse(bcuser.username) 
    # # 확인용



def logout(request):
    if request.session.get('user'): # 로그인 확인
        del(request.session['user']) # 세션의 생성 여부 확인

    return redirect('/') # 홈으로 들어감


def login(request):
    if request.method == "POST":
        form=LoginForm(request.POST) # 유효성 검사

        if form.is_valid(): # 유효성 검사 여부
            request.session['user']=form.user_id
            return redirect('/')
    else:
        form=LoginForm()
    # 로그인 실패시 재시도 할 수 있도록 login 페이지 열어줌
    return render(request, 'login.html', {'form':form})


# views.py에서는 templates 폴더를 참조하고 있으므로
# 요청이 들어왔을 때 Django에 있는 register.html을 참조하는 메소드 구현
def register(request):
    if request.method == "GET":
        return render(request, 'register.html') # render 은 경로 전달
    elif request.method == "POST":
        # request로 받을때 넘어오는 값이 없으면 nullpoint error 가 발생되므로  None 처리
        username=request.POST.get('username', None)
        useremail=request.POST.get('useremail', None)
        password=request.POST.get('password', None)
        re_password=request.POST.get('re-password', None)

        res_data={}

        if not(username and useremail and password and re_password):
            res_data['error']="모든 값을 입력해야 합니다."
        elif password != re_password:
            res_data['error']="비밀번호가 일치하지 않습니다."
        else:
            # 입력받은 값을 변수방에 저장하여 데이터베이스(models)에 전달
            bcuser = Bcuser(
                username=username, 
                # 평문이 아닌 암호화를 통하여 설정
                useremail=useremail,
                password = make_password(password)
            ) 
            bcuser.save() # 저장

        return render(request, 'register.html', res_data)





    # form py로 대체
    #------------
    #     return render(request, 'login.html') # render 은 경로 전달
    # elif request.method == "POST":
    #     # request로 받을때 넘어오는 값이 없으면 nullpoint error 가 발생되므로  None 처리
    #     username=request.POST.get('username', None)
    #     password=request.POST.get('password', None)

    #     res_data={}

    #     if not(username and password):
    #         res_data['error']="모든 값을 입력해야 합니다."
    #     else:
    #         # 데이터베이스 안에 있는 username과 입력하고 들어온 username이 일치하는 정보가 있는지 점검
    #         # bcuser 
    #         bcuser = Bcuser.objects.get(username=username)  # db에 데이터가 있으면 bcuser에 할당 된다 
    #         if  check_password(password, bcuser.password): # bcuser.password : 데이터 베이스에서 가져온 값
    #             # 비밀번호가 일치, 로그인 처리를!
    #             # 세션영역
    #             request.session['user']=bcuser.id
    #             # redirect
    #             # / 를 작성해주면 root 페이지 흔히 home 페이지로 이동
    #             return redirect('/')

    #         else:
    #             res_data['error']="비밀번호가 일치하지 않습니다."

    #     return render(request, 'login.html', res_data)



    # return render(request, "login.html", res_data)