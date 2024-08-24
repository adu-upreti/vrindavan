from django.db import models

class GenerateImage(models.Model):
    imag = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=None)
