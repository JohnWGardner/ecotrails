# Generated by Django 4.2.16 on 2024-12-10 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0008_alter_recommendation_destination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='destination',
        ),
    ]