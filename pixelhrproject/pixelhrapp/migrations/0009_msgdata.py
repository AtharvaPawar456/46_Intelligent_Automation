# Generated by Django 4.2.2 on 2024-04-07 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelhrapp', '0008_rename_llmsuggesstion_leave_llmsuggest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msgdata',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='', max_length=255)),
                ('shortdesc', models.TextField()),
            ],
        ),
    ]
