# Generated by Django 3.2.6 on 2022-03-23 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_alter_root_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='root',
            name='path',
            field=models.CharField(max_length=200),
        ),
    ]