# Generated by Django 5.1 on 2024-08-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logsign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
