from django.shortcuts import render

# Create your views here.
def LandingPageView(request):
    return render(request, 'landingpage.html')