# Generated by Django 3.2.6 on 2022-03-23 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='youtube',
            fields=[
                ('id_ytb', models.AutoField(primary_key=True, serialize=False)),
                ('id_song', models.IntegerField(default=0)),
                ('url', models.URLField()),
            ],
        ),
    ]
