# Generated by Django 2.1.7 on 2021-06-11 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FoodDelivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='Food_images')),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FoodImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='Food_images')),
            ],
        ),
        migrations.CreateModel(
            name='FoodRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='Restaurant_images')),
                ('location', models.CharField(max_length=200)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='FoodDelivery.City')),
            ],
        ),
        migrations.CreateModel(
            name='RestImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='Restaurant_images')),
                ('resto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.Restaurants')),
            ],
        ),
        migrations.CreateModel(
            name='Rrating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.Restaurants')),
            ],
        ),
        migrations.CreateModel(
            name='Rtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtype', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='restaurants',
            name='rtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.Rtype'),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='FoodDelivery.UserDetails'),
        ),
        migrations.AddField(
            model_name='foodrating',
            name='restau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.Restaurants'),
        ),
        migrations.AddField(
            model_name='foodimage',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.Restaurants'),
        ),
        migrations.AddField(
            model_name='food',
            name='fcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.FoodCategory'),
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.Restaurants'),
        ),
    ]
