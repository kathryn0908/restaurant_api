# Generated by Django 3.0.7 on 2020-07-08 15:26

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_researcher_app', '0023_auto_20200706_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='images',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
