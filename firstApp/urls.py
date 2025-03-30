from django.urls import path
from .views import *


urlpatterns = [
    path('', LandingPageView, name='landingpage'),
    path('about', AboutPageView, name='aboutpage'),
    path('service', ServicePageView, name='servicepage'),
    path('products', ProductPageView, name='productpage'),
    path('review', ReviewPageView, name='reviewpage'),
    path('contact', ContactPageView, name='contactpage')
]