from django.shortcuts import render
from logsign.models import *
from adminpage.models import Add_Team

def Home(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            full_name = profile.full_name
            first_name = full_name.split(' ')[0]
        except Profile.DoesNotExist:
            first_name = None
    else:
        first_name = None

    team_list = Add_Team.objects.all()

    context = {
        'teamlist': team_list,
    }
    
    if first_name:
        context['first_name'] = first_name

    return render(request, 'user/index.html', context)
