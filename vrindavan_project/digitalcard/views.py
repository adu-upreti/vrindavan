from django.shortcuts import render
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.conf import settings
from logsign.models import Profile
import os
import qrcode

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def create_profile_qr_code(user):
    profile = Profile.objects.get(user=user)
    data = f"Name: {profile.full_name}\nLocation: {profile.location}\nPhone: {profile.phone}\nGmail: {profile.user}"
    img = generate_qr_code(data)
    
    
    filename = f"{profile.full_name}_qr.png"
    file_path = os.path.join(settings.MEDIA_ROOT, 'qrcodes', filename)
    
  
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
   
    img.save(file_path)
    
    # Return the relative URL to the image
    return os.path.join('qrcodes', filename)

from django.core.cache import cache

@login_required
def MyCard(request):
    if request.user.is_authenticated:
        cache_key = f"qr_image_path_{request.user.id}"
        qr_image_path = cache.get(cache_key)

        if not qr_image_path:
            qr_image_path = create_profile_qr_code(request.user)
            cache.set(cache_key, qr_image_path) 

        qr_image_url = os.path.join(settings.MEDIA_URL, qr_image_path)
        
        context = {
            'qr_image_url': qr_image_url,
            'qr_image_name': qr_image_path.split('/')[-1]
        }
        return render(request, 'user/mycard.html', context)

