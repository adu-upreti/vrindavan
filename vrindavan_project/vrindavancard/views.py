from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import qrcode
import io
from logsign.models import *
from .models import GenerateImage



@login_required(login_url='adminlogin')
def MyCard(request):
    try:
        mydata = Profile.objects.get(user=request.user)
        qr_data = (
            f"Name: {mydata.full_name}\n"
            f"Email: {mydata.user.email}\n"
            f"Location: {mydata.location}\n"
            f"Phone: {mydata.phone if mydata.phone else 'N/A'}"
        )
    except Profile.DoesNotExist:
        return render(request, 'user/index.html')

    img = generate_qr_code(qr_data)

    image_io = io.BytesIO()
    img.save(image_io, format='PNG')

    image_file = ContentFile(image_io.getvalue(), name='vrindavan-card.png')

    qr_image = GenerateImage.objects.create(imag=image_file)

    context = {'img': qr_image}

    return render(request, 'user/mycard.html', context)


def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    return image


