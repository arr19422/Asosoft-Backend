# Generated by Django 3.2.3 on 2021-06-05 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_athlete_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='local_score',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='match',
            name='visiting_score',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
