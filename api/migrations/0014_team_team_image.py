# Generated by Django 3.2.3 on 2021-06-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20210601_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
