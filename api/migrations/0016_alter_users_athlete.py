# Generated by Django 3.2.3 on 2021-06-01 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20210601_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='athlete',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_athlete', to='api.athlete'),
        ),
    ]
