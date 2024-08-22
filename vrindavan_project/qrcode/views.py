from django.shortcuts import render

def MyCard(request):

    return render(request, 'user/mycard.html')
