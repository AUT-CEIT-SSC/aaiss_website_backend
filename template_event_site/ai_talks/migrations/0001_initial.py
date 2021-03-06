# Generated by Django 2.2.3 on 2019-07-09 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('position', models.CharField(max_length=300)),
                ('bio', models.TextField()),
                ('abstract', models.TextField()),
                ('image_path', models.CharField(max_length=300)),
                ('date_and_time', models.CharField(max_length=300)),
                ('talk_location', models.CharField(max_length=300)),
                ('talk_title', models.CharField(max_length=300)),
            ],
        ),
    ]
