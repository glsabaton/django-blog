# Generated by Django 3.1.1 on 2020-10-09 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='xxx', max_length=100),
        ),
    ]