from django.shortcuts import render, redirect
from django.template import loader

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def indexPage(request):
    template = loader.get_template('main/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, password=password, username=username)

        if user is not None:
            login(request, user)
            redirect('index')

    template = loader.get_template('main/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            message.success(request, 'Account was successfully created for ' +  user)
            return redirect('login')

    template = loader.get_template('main/register.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))
