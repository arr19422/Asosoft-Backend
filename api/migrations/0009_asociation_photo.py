# Generated by Django 3.2 on 2021-05-30 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210519_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='asociation',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
