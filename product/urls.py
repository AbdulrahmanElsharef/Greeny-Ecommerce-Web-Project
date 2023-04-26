from django.urls import path 

from .views import ProductList ,product_list_debug, ProductDetail , add_review,BrandList,BrandDetail

from .api import product_list_api , ProductListAPI,ProductDetailAPI,BrandListAPI,BrandDetailAPI

app_name = 'product'

urlpatterns = [
    
    # api
    path('api/list' , product_list_api),
    path('api/list/cbv/brands' , BrandListAPI.as_view()),
    path('api/list/cbv/brands/<slug:slug>' , BrandDetailAPI.as_view()),
    path('api/list/cbv' , ProductListAPI.as_view()),
    path('api/list/cbv/<slug:slug>' , ProductDetailAPI.as_view()),
    
    path('',ProductList.as_view(),name='product_list'),
    path('debug',product_list_debug,name='product_list_debug'),
    path('<slug:slug>',ProductDetail.as_view(),name='product_detail'),
    path('<slug:slug>/add-review',add_review,name='add_review'),
    path('brands/' , BrandList.as_view() , name='brand_list'),
    path('brands/<slug:slug>' , BrandDetail.as_view() , name='brand_detail'),
    
    

]
