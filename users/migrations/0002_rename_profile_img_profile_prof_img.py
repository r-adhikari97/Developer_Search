# Generated by Django 4.2 on 2023-10-30 05:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="profile_img",
            new_name="prof_img",
        ),
    ]
