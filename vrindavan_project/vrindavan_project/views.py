from django.shortcuts import render
from logsign.models import *
from django.contrib.auth.decorators import login_required


def Home(request):
    if request.user.is_authenticated:
        full_name = Profile.objects.get(user=request.user).full_name
        first_name = full_name.split(' ')[0]
    else:
        first_name = "Guest"

    return render(request, 'user/index.html', {'first_name': first_name})


