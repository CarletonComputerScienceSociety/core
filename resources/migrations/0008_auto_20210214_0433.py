# Generated by Django 3.1.4 on 2021-02-14 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0007_resource'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourcePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='resource',
            name='category',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='resource_type',
        ),
        migrations.AddField(
            model_name='resource',
            name='order',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='resource',
            name='organization',
            field=models.CharField(default='N/A', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='ResourcePageSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('description', models.TextField()),
                ('order', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('resource_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.resourcepage')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_page_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.resourcepagesection'),
        ),
    ]
