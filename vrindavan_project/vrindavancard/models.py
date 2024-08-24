from django.db import models

class GenerateImage(models.Model):
    imag = models.ImageField(upload_to='qr_codes/')

    def __str__(self):
        return self.imag.name
