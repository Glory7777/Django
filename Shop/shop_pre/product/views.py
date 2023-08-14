from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm #같은 기능 이라 RegisterForm 이지만 헷갈릴 수 있기에 애칭을 정해줌


from django.utils.decorators import method_decorator
from bcuser.decorators import admin_required

from .serializers import ProductSerializer
from rest_framework import mixins
from rest_framework import generics

# ListView : ListView를 사용하면 데이터베이스에서 목록을 가져와서 
# 템플릿에 어떤 데이터 타입이든 쉽게 전달하는 작업을 수행해줌
class ProductList(ListView):
    model=Product
    context_object_name='product_list'
    template_name='product.html'
    # paginate_by = 10 # 한페이지에 최대 10개씩 표시
    
    
@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name='register_product.html'
    form_class=RegisterForm
    success_url='/product/'
    
    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'), 
            price=form.data.get('price'), 
            description=form.data.get('description'), 
            stock=form.data.get('stock') )
        product.save()
        
        return super().form_valid(form)
    
class ProductDetail(DetailView):
    queryset = Product.objects.all()
    context_object_name='product'
    template_name='product_detail.html'
        
        # **kwargs : 함수에 정해지지 않은 매개변수의 가변갯수을 활용하여 오버라이딩함
        # 상세정보의 필드를 가변적으로 선택하여 보여줄 수 있음
    def get_context_data(self, **kwargs):
        # 기본적인 Product의 데이터 가져오기
        context=super().get_context_data(**kwargs)
        # Order 의 OrderForm에서 받아온 데이터 추가
        context['form']=OrderForm(self.request)
        return context 
    
# GenericAPIView : RestFulAPI의 기본 동작을 제공 views
# ListModelMixin : views에서 필요로하는 메서드를 제공    
class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    # RestFulAPI 타입으로 Product데이터베이스 변환
    # serializer_class : Product데이터를 JSON 형태로 반환
    serializer_class=ProductSerializer
    
    def get_queryset(self):
        # select * from Product order by;
        # Product의 모든 데이터를 id로 정렬하여 반환하라
        return Product.objects.all().order_by('id')
    
    def get(self, request, *args, **kwargs):
        # list() : ListModelMixin 에서 제공
        return self.list(request, *args, **kwargs)
    
    
# RetrieveModelMixin의 retrieve(): DRF을 사용하여 특정 데이터의 상세정보를 제공하는 API Views
class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class=ProductSerializer
    
    def get_queryset(self):
        return Product.objects.all().order_by('id')
    
    def get(self, request, *args, **kwargs):
        # retrieve() : RetrieveModelMixin의 retrieve()
        return self.retrieve(request, *args, **kwargs)