from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile


def Login(request):
    data = {
        'dashboard_active_page': 'active'
    }


    if request.method == "GET":
        return render(request, "user/login.html", data)
    
    elif request.method == "POST":
        form_username = request.POST['username']
        form_password = request.POST['password']
        user_obj = authenticate(username=form_username, password=form_password)
        if user_obj:
            login(request, user=user_obj)
            if user_obj.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            return render(request, "user/login.html", {'error': 'Invalid credentials'})
    else:
        print("unknown")




def register(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        location = request.POST.get('location', '')
        phone = request.POST.get('phone', '')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                Profile.objects.create(user=user, location=location, phone=phone)

                messages.success(request, 'Your account has been created successfully. Please log in.')
                return redirect('adminlogin')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'user/register.html')



@login_required
def admin_dashboard(request):
    data = {
        'dashboard_active_page': 'active'
    }
    return render(request, "adminfile/dashboard.html", data)


@login_required
def Logout(request):
    logout(request)
    data = {
        'logout_active_page':'active'
    }
    return render(request, "user/login.html", data)