# Generated by Django 3.0.7 on 2020-06-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_researcher_app', '0008_favorite_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]