# Generated by Django 3.0.7 on 2020-06-30 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_researcher_app', '0006_auto_20200629_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='has_online_delivery',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='is_delivering_now',
            field=models.TextField(),
        ),
    ]
