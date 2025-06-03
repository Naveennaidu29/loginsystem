from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import employee
from.forms import SignupForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            if employee.objects.filter(email=email).exists():
                return render(request, 'signup.html', {'form':form, 'error':'account already exists please login'})
            else:
                form.save()
                return redirect('login')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            password = form.cleaned_data['password']

            user = employee.objects.filter(email=identifier).first() or employee.objects.filter(name=identifier).first()
            if user:
                if user.password == password:
                    return render(request, 'welcome.html', {'user': user})
                else:
                    return render(request, 'login.html', {'form': form, 'error': 'Incorrect password. Please try again or change password.'})
            else:
               return render(request, 'login.html', {'form': form, 'error': 'Account not found. Please sign up.'})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})