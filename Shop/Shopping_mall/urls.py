from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # 전체 상품 리스트
    path('create/', views.product_create, name='product_create'),  # 상품 생성
    path('<int:pk>/', views.product_detail, name='product_detail'),  # 상품 상세
    path('<int:pk>/edit/', views.product_update, name='product_update'),  # 상품 수정
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),  # 상품 삭제
]