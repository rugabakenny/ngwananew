# Generated by Django 3.2 on 2021-05-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carrental',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mokoro',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nightclub',
            name='description',
            field=models.CharField(default=111, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='travel',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
