# Generated by Django 3.0.7 on 2020-07-06 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_researcher_app', '0021_auto_20200706_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='starrating',
            name='review',
        ),
    ]
