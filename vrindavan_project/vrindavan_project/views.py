from django.shortcuts import render
from logsign.models import *

def Home(request):
    user_details = Profile.objects.all()

    datas = {
            'details': user_details,
    }



    return render(request, 'user/index.html', datas)