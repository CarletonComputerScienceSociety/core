# Generated by Django 3.1.4 on 2021-07-31 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MultipleChoiceOptions",
            new_name="MultipleChoiceOption",
        ),
    ]
