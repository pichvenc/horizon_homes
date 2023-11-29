from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as AuthUser
from django.shortcuts import render, redirect, get_object_or_404

from horizon_main.forms import LoginForm, RegisterForm, ViewRequestForm
from horizon_main.models import UserProfile, Property, RequestViewing, ContactRequest


# Create your views here.
def home(request):
    all_properties = Property.objects.all()
    return render(request, 'index.html', {"properties": all_properties})


def register_user(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {"form": form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            phone_number = form.cleaned_data['phone_number']
            if password != confirm_password:
                messages.error(request, 'Passwords do not match')
                return render(request, 'register.html', {"form": form})
            else:
                user = AuthUser.objects.create_user(username=username, password=password, email=email)
                new_user = UserProfile.objects.create(user=user, phone_number=phone_number)
                new_user.user.first_name = firstname
                new_user.user.last_name = lastname
                new_user.save()
                messages.success(request, "Registration Successful")
                return redirect('login')
        messages.error(request, "Registration Failed")
        return render(request, 'register.html', {"form": form})


def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {"form": form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user=user)
                messages.success(request, 'Welcome back')
                return redirect('home')
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html', {"form": form})


def logout_user(request):
    logout(request)
    return redirect('login')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    elif request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        title = request.POST['title']
        description = request.POST['description']
        ContactRequest.objects.create(name=name, email=email, title=title, description=description)
        messages.success(request, 'Submitted successfully')
        return render(request, 'contact.html')
    messages.error(request, 'There was a problem during submission. Please try again')
    return render(request, 'contact.html')


def properties(request):
    all_properties = Property.objects.all()
    return render(request, 'properties.html', {"properties": all_properties})


@login_required
def single_property(request, property_id):
    the_property = Property.objects.get(pk=property_id)
    form = ViewRequestForm()
    return render(request, 'property-single.html', {"property": the_property, "form":form})


def book_viewing(request, property_id):
    user = get_object_or_404(UserProfile, user=request.user)
    the_property = Property.objects.get(pk=property_id)
    if request.method == 'POST':
        form = ViewRequestForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['preferred_date']
            RequestViewing.objects.create(customer=user, property=the_property, preferred_date=date)
            messages.success(request, "Request Successful.")
            return redirect('properties')
        messages.error(request, "Enter a valid date")
        return render(request, 'property-single.html', {"property": the_property, "form": form})


def page_not_found(request):
    return render(request, '404.html')