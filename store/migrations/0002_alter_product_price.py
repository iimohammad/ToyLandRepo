# Generated by Django 4.2 on 2024-03-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10),
        ),
    ]
