import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django 
django.setup()

from faker import Faker
import random
from product.models import Product , Brand , ProductImages , ProductReview


def seed_brand(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg']
    
    for x in range(n):
        Brand.objects.create(
            name = fake.name() ,
            image = f"brand/{images[random.randint(0,11)]}"
        )
    print(f'{n} Brand Seeded')



def seed_product(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
    flags = ['New','Feature','Sale']

    for x in range(n):
        Product.objects.create(
            name = fake.name() , 
            image = f"products/{images[random.randint(0,12)]}" , 
            price = round(random.uniform(20.99,99.99),2) , 
            sku = random.randint(1000,1000000) , 
            subtitle = fake.text(max_nb_chars=300) , 
            description = fake.text(max_nb_chars=5000) , 
            flag = flags[random.randint(0,2)] , 
            brand = Brand.objects.get(id=random.randint(1,120)),  
        )
    print(f'{n} Products Seeded')


def seed_product_images(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
    for x in range(n): 
        ProductImages.objects.create(
            product = Product.objects.get(id=random.randint(1,5000)) , 
            image = f"productimages/{images[random.randint(0,12)]}" , 
        )
    print(f'{n} Products Images Seeded')

# seed_brand(100)
# seed_product(5000)
seed_product_images(10000)