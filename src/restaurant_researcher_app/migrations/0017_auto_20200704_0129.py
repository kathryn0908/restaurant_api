# Generated by Django 3.0.7 on 2020-07-04 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_researcher_app', '0016_review_restaurant_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='restaurant_name',
            new_name='name',
        ),
    ]