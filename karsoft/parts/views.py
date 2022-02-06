from django.shortcuts import render, HttpResponse, redirect
from .models import Meals, Reserve, Users, InterfaceControl
from .forms import ReserveForm

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)


def contact_us(request):
    return render(request, "contact.html", {})


def mealspage(request):

    meals = Meals.objects.all()
    context = {'meals': meals}
    return render(request, "meals.html", context)

def homepage1(request):

    context = {}
    return render(request, "home1.html", context)


def about_us(request):
    return render(request, "about.html", {})

def ReserveCreate(request):

    if request.POST:
        commit_form = ReserveForm(request.POST)
        if commit_form.is_valid():
            commit_form.save()
            return render(request, 'home1.html', {"message":"Success"})

    return render(request, "home1.html", {})

def ReserveRetrieve(request):
    reserve = Reserve.objects.all()
    context = {'reserve': reserve}
    return render(request, "ReserveRetrieve.html", context)

def test(request):
    context = {}

    return render(request, "test.html", context)

def index(request):
    context = {}

    return render(request, "index.html", context)


from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/login')

