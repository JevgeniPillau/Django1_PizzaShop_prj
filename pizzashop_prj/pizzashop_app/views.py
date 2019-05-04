from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from pizzashop_app.forms import OwnerForm, PizzeriaForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def home(request):
    return redirect(pizzashop_app_home)


@login_required(login_url='sign-in/')
def pizzashop_app_home(request):
    return render(request, 'pizzashop_app/home.html')

@login_required(login_url='sign-in/')
def pizzashop_app_account(request):
    return render(request, 'pizzashop_app/account.html')

@login_required(login_url='sign-in/')
def pizzashop_app_pizza(request):
    return render(request, 'pizzashop_app/pizza.html')

def pizzashop_app_sign_up(request):
    owner_form = OwnerForm()
    pizzeria_form = PizzeriaForm()

    if request.method == 'POST':
        owner_form = OwnerForm(request.POST)
        pizzeria_form = PizzeriaForm(request.POST, request.FILES)

        if owner_form.is_valid() and pizzeria_form.is_valid():
            new_owner = User.objects.create_user(**user_form.cleaned_data)
            new_pizzeria = pizzeria_form.save(commit=False)
            new_pizzeria.owner = new_owner
            new_pizzeria.save()

            login(request, authenticate(
                username=user_form.cleaned_data('username'),
                password=user_form.cleaned_data('password')
            ))
            return redirect(pizzashop_app_home)

    return render(request, 'pizzashop_app/sign_up.html', {
        'owner_form': owner_form,
        'pizzeria_form': pizzeria_form
    })
