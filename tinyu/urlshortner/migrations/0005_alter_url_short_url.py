# Generated by Django 4.2.6 on 2023-10-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("urlshortner", "0004_remove_url_time_created_alter_url_short_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="url",
            name="short_url",
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
