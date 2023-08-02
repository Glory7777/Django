from django import forms
from .models import Bcuser
from django.contrib.auth.hashers import check_password

# forms.Form : 유효성 검사를 진행하는 클래스로 상속받아서
class LoginForm(forms.Form):
    # 유효성 검사 : 값을 입력하지 않았을 때 기본적으로 영문 메세지가 출력됨
    # 사용자가 원하는 메세지를 구현하여 출력할 수 있음
    username= forms.CharField(
        error_messages={
            'required': '사용자 이름을 입력해주세요'
            },        
        max_length=32, label="사용자 이름")

    password= forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
            },
        widget=forms.PasswordInput, label="비밀번호" )

    def clean(self):
        cleaned_data = super().clean() # super() : 부모클래스(forms)의 생성자(super()를 통하여 Form 클래스 참조
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                bcuser = Bcuser.objects.get(username=username)
            except Bcuser.DoesNotExist:
                self.add_error('username', '존재하지 않는 아이디 입니다.')
                return

            if not check_password(password, bcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.') # error 검출
            else:
                self.user_id=bcuser.id  # 로그인 성공한 아이디를 user_id에 저장

        #오버로딩 오버라이딩

        #super()는 파이썬에서 부모 클래스의 메서드를 호출할 때 사용하는 함수
        #self는 현재 클래스의 인스턴스를 가리키는 참조 변수