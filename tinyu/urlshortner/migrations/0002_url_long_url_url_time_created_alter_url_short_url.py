# Generated by Django 4.2.6 on 2023-10-24 02:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("urlshortner", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="url",
            name="long_url",
            field=models.CharField(default="qwerty", max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="url",
            name="time_created",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="url",
            name="short_url",
            field=models.CharField(max_length=7),
        ),
    ]