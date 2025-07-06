from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import Group


class BaseRegisterView(CreateView):
    model = User # модель формы, которую реализует данный дженерик;
    form_class = BaseRegisterForm # форма, которая будет заполняться пользователем;
    template_name = 'sing/register.html' # шаблон который нужно открыть
    success_url = '/' # URL, на который нужно направить пользователя после успешного ввода данных в форму.


@login_required
def logout_page(request):
    if request.method == "POST":
        logout(request)
        return redirect('') 

    return render(request, 'sing/logout.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('news_list') 
    else:
        form = AuthenticationForm()
    return render(request, 'sing/login.html', {'form': form})


@login_required
def become_author(request):
    author_group, _ = Group.objects.get_or_create(name='authors')
    user = request.user
    if not user.groups.filter(name='authors').exists():
        user.groups.add(author_group)
    return redirect('news_list')  # Перенаправить куда нужно
