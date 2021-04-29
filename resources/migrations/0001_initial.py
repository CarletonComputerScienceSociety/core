# Generated by Django 3.1.4 on 2020-12-22 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JobPosting",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("url", models.CharField(max_length=150)),
                ("company", models.CharField(max_length=50)),
                ("found_date", models.DateField()),
                ("expiry_date", models.DateField()),
                (
                    "country",
                    models.CharField(
                        choices=[("c", "Canada"), ("u", "United States")], max_length=1
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("s", "suggested"), ("p", "public"), ("e", "expired")],
                        max_length=1,
                    ),
                ),
            ],
        ),
    ]
