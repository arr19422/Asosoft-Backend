# Generated by Django 3.2.3 on 2021-06-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_tournament_association'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='local_score',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='match',
            name='visiting_score',
            field=models.IntegerField(default=None),
        ),
    ]
