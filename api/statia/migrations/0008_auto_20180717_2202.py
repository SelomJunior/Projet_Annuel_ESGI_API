# Generated by Django 2.0.7 on 2018-07-17 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statia', '0007_matcheventplayer_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matcheventgoalkeeper',
            name='player',
        ),
        migrations.RemoveField(
            model_name='matcheventgoalkeeper',
            name='statsMatch',
        ),
        migrations.RemoveField(
            model_name='matcheventplayer',
            name='lastpassPlayer',
        ),
        migrations.DeleteModel(
            name='MatchEventGoalkeeper',
        ),
    ]