# Generated by Django 2.1.7 on 2021-06-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_caddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='caddress',
            name='mobile',
            field=models.CharField(default='8435587742', max_length=10),
        ),
    ]
