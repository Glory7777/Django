
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm #order의 RegisterForm
from product.models import Product
from bcuser.models import Bcuser
from .models import Order

class OrderCreate(FormView):
    form_class=RegisterForm
    success_url='/order/' # 또는 /product/
    
    #폼의 데이터 유효성 검사
    def form_valid(self, form):
        # transaction 블록 내에서 수행되는 모든 데이터베이스 연산은 원자성을 갖는다
        # 원자성(atomicity) : 블록 내에 연산 중에 하나라도 실패하면 모든 연산이 취소됨/ 데이터베이스가 작업하는 단위, 처리단위
        with transaction.atomic(): # 데이터베이스의 트랜젝션 시작 / 트랜젝션: 데이터베이스를 처리하는 단위, 작업단위, 세션 구역을 만들어 놔서 임계지역 만들어 
            # 폼 데이터에서 제품 id를 가져와서 저장
            prod = Product.objects.get(pk=form.data.get('product'))
            # 주문객체 생성
            order=Order(
                quantity=form.data.get('quantity'), # Product 데이터베이스에서 수량가져오기
                product= prod,   #제품 아이디
                bcuser= Bcuser.objects.get(email=self.request.session.get('user'))  #주문정보에 제품정보, 수량 담아둠

                )
            # 주문사항 저장
            order.save()
            # 제품의 재고가 줄어들어야 함
            prod.stock -= int(form.data.get('quantity'))
            # 제품의 변경사항(즉 재고)를 저장
            prod.save()
        return super().form_valid(form)

    # 폼의 데이터가 유효하지 않을 때 호출되는 메서드
    def form_invalid(self, form):
        #해당 제품의 정보를 갖고 리스트페이지로 redirect
        return redirect('/product/'+str(form.data.get('product')))
    
    def get_form_kwargs(self, **kwargs):
        kw=super().get_form_kwargs(**kwargs)
        # RegisterForm 에서 __init__ 생성자에 선언되어 있는 request 객체를 update
        kw.update({
            'request' : self.request
        })
        
        return kw
    
# 현재 세션에 있는 이메일에 해당하는 order객체를 필터링하여 주문 정보 가져옴
class OrderList(ListView):
    # model=Order #주문된 제품만 가져오므로 쿼리를 통해서 가져옴
    context_object_name='order_list'
    template_name='order.html'
        
        # bcuser__email : Order 모델에 bcuser라는 외래키가 존재하므로 bcuser 필드의 email 속성에 접근이 가능
    def get_queryset(self, **kwargs) :
        queryset=Order.objects.filter(bcuser__email=self.request.session.get('user'))
        return queryset
