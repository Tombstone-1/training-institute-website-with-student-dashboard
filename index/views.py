from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Batch
from .forms import SignUpForm, FeebackForm, Contact_usForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = Contact_usForm()
    if request.method == 'POST':
        form = Contact_usForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Your Submission has been received")
        else:
            messages.error(request, "oops! Something went wrong")

    context = {'form' : form}
    return render(request, 'contact.html', context)

def course(request):
    return render(request, 'course.html')

def course_details(request, coursetag):
    if coursetag == 'c-cpp':
        return render(request, 'course/c.html')
    elif coursetag == 'python':
        return render(request, 'course/python.html')
    elif coursetag == 'java':
        return render(request, 'course/java.html')
    elif coursetag == 'MERN':
        return render(request, 'course/mern.html')
    elif coursetag == 'full_stack_python':
        return render(request, 'course/full_stack.html')
    elif coursetag == 'full_stack_java':
        return render(request, 'course/full_stackjava.html')
    elif coursetag == 'DA':
        return render(request, 'course/DA.html')
    elif coursetag == 'devOps':
        return render(request, 'course/devops.html')
    elif coursetag == 'DS':
        return render(request, 'course/DS.html')
    elif coursetag == 'dbms':
        return render(request, 'course/dbms.html')
    elif coursetag == 'software_tester':
        return render(request, 'course/tester.html')
    else:
        return HttpResponse('<center><h1>Opps.. My bad 404 again</h1></center>')

def batch(request):
    tb_data = Batch.objects.all().order_by('start_date')
    context = {'data' : tb_data}
    return render(request, 'batch.html', context)

def signup(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        username = request.POST.get('username').lower()

        try:
            user = User.objects.get(username = username )
            messages.error(request, 'username is already taken')
        except User.DoesNotExist:
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                messages.success(request, 'You have sign up successfully.')
                return redirect("/sign_in")
            else:
                messages.warning(request, 'Registration Unsuccessful')

    form = SignUpForm()
    context = {'signup_form': form}
    return render(request, 'signup.html', context)    


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"you are now logged in as {username}.")
                return redirect("/dashboard")
        
        else:
            messages.warning(request, "Invalid username or Password.")
            return redirect("/sign_in")
    
    form = AuthenticationForm()
    context = {'signin_form' : form}
    return render(request, 'signin.html', context)
           

@login_required(login_url="/sign_in")
def feedback(request):
    feedback_form = FeebackForm()

    if request.method == 'POST':
        feedback_form = FeebackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            messages.success(request, "Thanks for your Valued feedback")
        else :
            messages.error(request, "Oops! something went wrong")
    
    content = {'feedback_form' : feedback_form}
    return render(request, 'feedback.html', content )

@login_required(login_url="/sign_in")
def dashboard(request):
    context = {}
    return render(request,'dashboard.html',context)

def signout(request):
    logout(request)
    messages.success(request, "User logged Out Successfully")
    return redirect("/")
