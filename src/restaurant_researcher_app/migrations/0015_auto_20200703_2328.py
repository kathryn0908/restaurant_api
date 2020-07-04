# Generated by Django 3.0.7 on 2020-07-03 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_researcher_app', '0014_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='restaurant_researcher_app.Restaurant'),
        ),
    ]