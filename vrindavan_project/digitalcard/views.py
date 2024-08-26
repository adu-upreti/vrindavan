from django.shortcuts import render
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
    data = f"Name: {profile.full_name}\nLocation: {profile.location}\nPhone: {profile.phone}"
    img = generate_qr_code(data)
    
    # Define the file path for saving the QR code
    filename = f"{profile.full_name}_qr.png"
    file_path = os.path.join(settings.MEDIA_ROOT, 'qrcodes', filename)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Save the QR code image
    img.save(file_path)
    
    # Return the relative URL to the image
    return os.path.join('qrcodes', filename)

@login_required
def MyCard(request):
    if request.user.is_authenticated:
        qr_image_path = create_profile_qr_code(request.user)
        
        # Construct the full URL for the image
        qr_image_url = os.path.join(settings.MEDIA_URL, qr_image_path)
        
        # Pass the URL to the template
        context = {
            'qr_image_url': qr_image_url,
            'qr_image_name': qr_image_path.split('/')[-1]  # Extract the image name for download
        }
        return render(request, 'user/mycard.html', context)

