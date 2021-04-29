# Generated by Django 3.1.4 on 2021-02-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0012_auto_20210214_0719"),
    ]

    operations = [
        migrations.AddField(
            model_name="resourcepagesection",
            name="status",
            field=models.CharField(
                choices=[("p", "public"), ("h", "hidden")], default="h", max_length=1
            ),
            preserve_default=False,
        ),
    ]
