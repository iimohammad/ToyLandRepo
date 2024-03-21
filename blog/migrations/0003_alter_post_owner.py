# Generated by Django 4.2 on 2024-03-21 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_remove_media_image_media_media_alter_media_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]