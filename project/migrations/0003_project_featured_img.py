# Generated by Django 4.2 on 2023-10-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0002_tag_project_vote_ratio_project_vote_total_review_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="featured_img",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
    ]
