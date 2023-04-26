# form
from rest_framework import serializers
from .models import Product , Brand , ProductReview,ProductImages


class ProductImagesSerailizer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['image']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = ProductReview
        fields = ['id','user','rate','review','date']
        
        
class ProductListSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    brand = serializers.StringRelatedField()
    price_with_tax = serializers.SerializerMethodField(method_name='price_wit')
    class Meta:
        model = Product
        fields = '__all__'
        
    def price_wit(self,product):
        return product.price*1.1
        
        
class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    reviews = ProductReviewSerializer(source='prduct_review',many=True)
    images = ProductImagesSerailizer(source='product_images',many=True)
    class Meta:
        model = Product
        fields = '__all__'
        
        
        
class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(source='product_brand',many=True)
    class Meta:
        model = Brand
        fields = '__all__'