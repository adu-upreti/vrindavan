from django.shortcuts import render
from logsign.models import *

def Home(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            full_name = profile.full_name
            first_name = full_name.split(' ')[0]
        except Profile.DoesNotExist:
            # Handle the case where the profile does not exist
            first_name = "User"  # Or you can provide a default value or create the Profile
    else:
        first_name = "Guest"

    return render(request, 'user/index.html', {'first_name': first_name})


