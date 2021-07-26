# Generated by Django 3.2.4 on 2021-06-24 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FoodDelivery', '0002_userdetails_city'),
        ('restaurant', '0010_restchefs_details'),
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prnum', models.IntegerField()),
                ('time', models.CharField(default='00:00 PM', max_length=100)),
                ('rest', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.restaurants')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='FoodDelivery.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingid', models.CharField(max_length=100)),
                ('ordertime', models.DateTimeField(auto_now=True)),
                ('delevirytime', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('status', models.IntegerField()),
                ('delivboy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='delivery.deliveryboy')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.food')),
                ('rest', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.restaurants')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='FoodDelivery.userdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='FoodDelivery.userdetails')),
            ],
            options={
                'unique_together': {('user', 'food')},
            },
        ),
    ]