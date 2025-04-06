from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import *
import calendar
from datetime import datetime, timedelta



def LandingPageView(request):
    """ landing page """
    return render(request, 'firstApp/landingpage.html')



def RegisterPageView(request):
    """Register a new user using a custom form"""
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('loginpage')
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'auth/register.html', {'form': form})


def LoginPageView(request):
    """ Login page view """
    if request.method == 'POST':
        email = request.POST.get('email')  # Get the email from the form
        password = request.POST.get('password')  # Get the password from the form

        # Debugging: Print email and password for debugging purposes
        print(f"Attempting to log in with email: {email}")

        # Attempt to authenticate the user using email and password
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # If user is authenticated, log them in
            print(f"Login successful for email: {email}")
            login(request, user)
            return redirect('dashboardpage')  # Redirect to the home page or wherever you'd like
        else:
            # If authentication fails, show an error message
            print(f"Authentication failed for email: {email}")
            messages.error(request, "Invalid email or password.")

    return render(request, 'auth/login.html')



def logoutView(request):
    """Logout the user and redirect to the landing page"""
    logout(request)
    return redirect('landingpage')


def CalenderPageView(request):
    """ Calendar page view that renders a calendar with dates only """
    
    # Get current date for dynamic month/year display
    today = datetime.today()
    month = today.month
    year = today.year
    
    # Generate calendar for the month
    cal = calendar.Calendar(firstweekday=6)  # Starts on Sunday
    month_days = cal.monthdayscalendar(year, month)
    
    # Build list of days
    days_of_week = []
    for week in month_days:
        week_days = []
        for day in week:
            if day != 0:  # If day is not 0, it is a valid day of the month
                week_days.append({
                    'day': day,
                    'is_current_month': True,
                })
            else:
                week_days.append({
                    'day': '',
                    'is_current_month': False,
                })
        days_of_week.append(week_days)
    
    # Pass month name and year dynamically
    month_name = calendar.month_name[month]
    
    # Render the template with the generated data
    return render(request, 'auth/calender.html', {
        'calendar_weeks': days_of_week,
        'month_name': month_name,
        'year': year,
    })




def RecordservicePageView(request):
    if request.method == 'POST':
        form = ServiceRenderedForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Service recorded successfully.")
            form = ServiceRenderedForm()
        else:
            print(form.errors)  # DEBUG
    else:
        form = ServiceRenderedForm()

    services = ServiceRendered.objects.order_by('-created_at')
    return render(request, 'auth/recordservice.html', {'form': form, 'services': services})




def CalculatePageView(request):
    """ calculate page """
    return render(request, 'auth/calculate.html')




@login_required(login_url='loginpage')
def DashboardPageView(request):
    user = request.user
    profile = getattr(user, 'profile', None)

    context = {
        'user': user,
        'profile': profile
    }

    return render(request, 'auth/dashboard.html', context)


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



def NotfoundPageView(request, exception):
    """ not found page """
    return render(request, 'auth/notfound.html', status=404)