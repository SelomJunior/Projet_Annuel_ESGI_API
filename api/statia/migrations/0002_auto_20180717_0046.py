# Generated by Django 2.0.7 on 2018-07-17 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='away_goal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_goal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='state',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
