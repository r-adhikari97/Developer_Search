# Generated by Django 4.2 on 2023-10-30 06:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_remove_profile_prof_img_profile_profile_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="location",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.profile",
                    ),
                ),
            ],
        ),
    ]