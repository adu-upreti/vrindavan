from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User



def Login(request):
    data = {
        'login_active_page':'active'
    }

    if request.method == "GET":
        return render(request, "adminfile/login.html", data)
    
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
            return render(request, "adminfile/login.html", {'error': 'Invalid credentials'})
    else:
        print("unknown")




def register(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'adminfile/register.html', {'error': 'Username already exists'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'adminfile/register.html', {'error': 'Email already exists'})
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('adminlogin')
        else:
            return render(request, 'adminfile/register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'adminfile/register.html')
    

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
    return render(request, "adminfile/login.html", data)