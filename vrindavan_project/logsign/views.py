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
        form_email = request.POST['username']  # Getting the email from the form
        form_password = request.POST['password']

        try:
            # Get the user object using the email
            user_obj = User.objects.get(email=form_email)
            # Authenticate using the username (which is the email in this case) and password
            user = authenticate(username=user_obj.username, password=form_password)

            if user:
                login(request, user=user)
                if user.is_superuser:
                    return redirect('admin_dashboard')
                else:
                    return redirect('user_dashboard')
            else:
                messages.error(request, 'Invalid credentials')
                return render(request, "user/login.html", data)
        
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials')
            return render(request, "user/login.html", data)
    
    else:
        return render(request, "user/login.html", data)




def register(request):
    if request.method == "POST":
        full_name = request.POST['name']  # Full Name field
        email = request.POST['email']  # Email will serve as the username
        password = request.POST['password']
        password2 = request.POST['password2']
        location = request.POST.get('location', '')
        phone = request.POST.get('phone', '')

        if password == password2:
            if User.objects.filter(username=email).exists():
                messages.error(request, 'Email already exists')
            else:
                # Create the user using the email as the username
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()

                # Create the profile with the full name, location, and phone number
                Profile.objects.create(user=user, full_name=full_name, location=location, phone=phone)

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
    return render(request, "user/index.html", data)