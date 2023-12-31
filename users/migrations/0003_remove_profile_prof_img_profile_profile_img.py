# Generated by Django 4.2 on 2023-10-30 05:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_rename_profile_img_profile_prof_img"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="prof_img",
        ),
        migrations.AddField(
            model_name="profile",
            name="profile_img",
            field=models.ImageField(
                blank=True,
                default="profiles/user-default.png",
                null=True,
                upload_to="profiles/",
            ),
        ),
    ]
