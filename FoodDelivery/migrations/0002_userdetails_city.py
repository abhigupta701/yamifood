# Generated by Django 2.1.7 on 2021-06-22 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FoodDelivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='city',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='FoodDelivery.City'),
        ),
    ]
