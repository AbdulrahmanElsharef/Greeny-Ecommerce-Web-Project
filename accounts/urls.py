from django.urls import path
from .views import profile , signup

app_name = 'accounts'


urlpatterns = [
    path('profile/' , profile , name='profile'),
    path('signup/' , signup , name='signup'),
]
