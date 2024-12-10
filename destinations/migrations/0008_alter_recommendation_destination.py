# Generated by Django 4.2.16 on 2024-12-10 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0007_recommendation_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='destinations.destination'),
        ),
    ]