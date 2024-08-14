from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('machines')
            else:
                form.add_error(None, 'Incorrect login or password entered')
    else:
        form = LoginForm()

    return render(request, 'catalog/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('machines')
