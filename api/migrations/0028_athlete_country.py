# Generated by Django 3.2.3 on 2021-06-05 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20210604_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='country',
            field=models.CharField(choices=[('Guatemala', 'Guatemala'), ('El Salvador', 'El Salvador'), ('Honduras', 'Honduras'), ('Nicaragua', 'Nicaragua'), ('Costa Rica', 'Costa Rica'), ('Panamá', 'Panamá'), ('México', 'México')], default='Guatemala', max_length=32),
        ),
    ]
