# Generated by Django 4.2 on 2024-03-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorderitem',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
