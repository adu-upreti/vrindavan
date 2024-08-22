from django.shortcuts import render



def UserLogin(request):

    return render(request, 'user/login.html')


def UserSignin(request):

    return render(request, 'user/register.html')