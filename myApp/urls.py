from django.urls import path
from .views import homepage, products, contact_us

urlpatterns = [
    path('', homepage, name='homepage'),
    path('products/', products, name='products'),
    path('contact/', contact_us, name='contact_us'),
]