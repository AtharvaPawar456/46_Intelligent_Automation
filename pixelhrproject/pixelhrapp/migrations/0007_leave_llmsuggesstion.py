# Generated by Django 4.2.2 on 2024-04-06 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelhrapp', '0006_employaccdata_communicationvalue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='llmsuggesstion',
            field=models.CharField(default='', max_length=50),
        ),
    ]
