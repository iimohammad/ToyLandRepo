# Generated by Django 4.2 on 2024-03-22 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchase', '0004_remove_cart_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(default=2, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
