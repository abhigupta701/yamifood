# Generated by Django 2.1.7 on 2021-06-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_auto_20210616_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='mobile',
            field=models.CharField(default='0000000000', max_length=15),
        ),
    ]
