# view 
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from .models import Product,Brand
from .serializers import ProductListSerializer,ProductDetailSerializer,BrandSerializer,BrandDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .mypagination import ProductPagination
from rest_framework import filters
from .myfilters import ProductFilter
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def product_list_api(request):
    query1 = Product.objects.all()[:20]
    data1 = ProductListSerializer(query1,many=True).data
    return Response({'data':data1})
    
    
class ProductListAPI(generics.ListCreateAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name','brand','flag']
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_class = ProductFilter
    filterset_fileds = ['name']
    # search_fields = ['name', 'brand']
    ordering_fields = ['price','brand']
    permission_classes = [IsAuthenticated]
    
    
class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'
    
    
    
class BrandListAPI(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    
    
class BrandDetailAPI(generics.RetrieveAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all()
    lookup_field = 'slug'