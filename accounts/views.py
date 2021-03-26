from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm, UserRegisterForm

 

def login_registration_view(request):

    # login view
    next = request.GET.get('next')
    l_form = UserLoginForm(request.POST or None)
    if l_form.is_valid():
        username = l_form.cleaned_data.get('username')
        password = l_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        else:
            return redirect('/')

    # registration view
    # next = request.GET.get('next')
    r_form = UserRegisterForm(request.POST or None)
    if r_form.is_valid():
        user = r_form.save(commit=False) # Holds the data 
        password = r_form.cleaned_data.get('password')
        user.set_password(password) # creates text into hash
        user.save()
        new_user = authenticate(username=user.username, password=password,)
        login(request, new_user)
        if next:
            return redirect(next)
        else:
            return redirect('/')

    context = {
        'l_form': l_form,
        'r_form': r_form,
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")


def csrf_failure(request, reason=""):
    reason = 'Time Out'
    return render(request, 'access_denied.html',{'reason':reason})