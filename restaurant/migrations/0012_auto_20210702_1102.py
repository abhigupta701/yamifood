# Generated by Django 2.1.7 on 2021-07-02 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_foodimage_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('post', models.CharField(max_length=100)),
                ('rest', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.Restaurants')),
            ],
        ),
        migrations.RemoveField(
            model_name='foodrating',
            name='restau',
        ),
        migrations.AddField(
            model_name='foodrating',
            name='food',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.Food'),
        ),
    ]
