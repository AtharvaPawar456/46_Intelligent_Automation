# Generated by Django 4.2.2 on 2024-04-07 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelhrapp', '0014_employaccdata_checkin_employaccdata_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employaccdata',
            name='Checkin',
            field=models.CharField(default='12:00', max_length=50),
        ),
        migrations.AlterField(
            model_name='employaccdata',
            name='Checkout',
            field=models.CharField(default='19:00', max_length=50),
        ),
    ]
