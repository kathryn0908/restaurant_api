# Generated by Django 3.0.7 on 2020-07-03 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_researcher_app', '0010_auto_20200630_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='review',
            name='restaurant',
            field=models.ManyToManyField(to='restaurant_researcher_app.Restaurant'),
        ),
    ]
