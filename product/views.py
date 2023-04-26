from django.shortcuts import render , redirect
from .models import Product , Brand
from django.views.generic import ListView , DetailView
from .forms import ProductReviewForm
from django.db.models.aggregates import Min ,Max , Avg , Count , Sum
from django.db.models import Q  , F

from django.views.decorators.cache import cache_page


@cache_page(60)
def product_list_debug(request):
    # data = Product.objects.filter(
    #     Q(price__gt=50) &
    #     Q(name__contains='David'))
    
    '''
        - prefetch_related : many-tomany
        - select_related : one-to-one , one-to-many
    '''
    
    data = Product.objects.annotate(newcol=F('price')*1.1)
    return render(request,'product/product_test.html',{'data':data})



from django.utils.decorators import method_decorator

class ProductList(ListView):
    model = Product
    paginate_by = 50
    extra_context = {'all_count' : Product.objects.all().count()}
    
    
    
    
class ProductDetail(DetailView):
    model = Product
    
    
    def get_context_data(self, **kwargs):
        product = self.get_object()
        context = super().get_context_data(**kwargs)
        context["related_products"] = Product.objects.filter(brand=product.brand)[:10] 
        return context
    

def add_review(request,slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.product = product
            myform.save()
    return redirect(f'/products/{product.slug}')



class BrandList(ListView):
    model = Brand
    paginate_by = 50
    extra_context = {'all_count' : Brand.objects.all().count()}
    
    
    
class BrandDetail(ListView):
    model = Product
    paginate_by = 50
    template_name = 'product/brand_detail.html'
    
    @method_decorator(cache_page(60))
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    
    