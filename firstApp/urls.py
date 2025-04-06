from django.urls import path
from .views import *


urlpatterns = [
    path('', LandingPageView, name='landingpage'),
    path('register', RegisterPageView, name='registerpage'),
    path('login', LoginPageView, name='loginpage'),
    path('logout', logoutView, name='logout'),
    path('dashboard', DashboardPageView, name='dashboardpage'),
    path('store', StorePageView, name='storepage'),
    path('book-session', BookPageView, name='booksessionpage'),
    path('user-review', UserReviewPageView, name='userreviewpage'),
    path('about', AboutPageView, name='aboutpage'),
    path('service', ServicePageView, name='servicepage'),
    path('products', ProductPageView, name='productpage'),
    path('review', ReviewPageView, name='reviewpage'),
    path('contact', ContactPageView, name='contactpage')
]