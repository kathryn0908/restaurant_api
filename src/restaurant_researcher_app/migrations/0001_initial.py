# Generated by Django 3.0.7 on 2020-06-24 18:17

from django.db import migrations, models
import jsonfield.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('cuisines', models.CharField(max_length=50)),
                ('timings', models.TextField()),
                ('url', models.URLField()),
                ('address', models.TextField()),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('has_online_delivery', models.BooleanField()),
                ('is_delivering_now', models.BooleanField()),
                ('average_cost_for_two', models.PositiveIntegerField()),
                ('highlights', jsonfield.fields.JSONField()),
            ],
        ),
    ]
