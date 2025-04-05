from django.shortcuts import render



def LandingPageView(request):
    """ landing page """
    return render(request, 'firstApp/landingpage.html')



def RegisterPageView(request):
    """ register page """
    return render(request, 'auth/register.html')


def LoginPageView(request):
    """ login page """
    return render(request, 'auth/login.html')


def DashboardPageView(request):
    """ dashboard """
    return render(request, 'auth/dashboard.html')


def StorePageView(request):
    """ store page """
    return render(request, 'auth/store.html')


def BookPageView(request):
    """ book page """
    return render(request, 'auth/booksession.html')


def UserReviewPageView(request):
    """ review page """
    return render(request, 'auth/review.html')


def AboutPageView(request):
    """ about page """
    return render(request, 'firstApp/aboutpage.html')


def ServicePageView(request):
    """ service page """
    return render(request, 'firstApp/servicepage.html')


def ProductPageView(request):
    """ products page """
    return render(request, 'firstApp/productpage.html')


def ReviewPageView(request):
    """ review page """
    return render(request, 'firstApp/reviewpage.html')


def ContactPageView(request):
    """ contact page """
    return render(request, 'firstApp/contactpage.html')