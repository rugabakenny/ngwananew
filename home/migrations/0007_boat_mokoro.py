# Generated by Django 3.2 on 2021-04-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='')),
                ('location', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mokoro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='')),
                ('location', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
            ],
        ),
    ]
