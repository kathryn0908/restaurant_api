# Generated by Django 3.0.7 on 2020-06-26 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_researcher_app', '0002_auto_20200626_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]