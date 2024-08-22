# Generated by Django 4.2.6 on 2023-11-10 04:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_one_way_type_package_type_round_trip_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='drivertableshow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Starting', models.CharField(max_length=30)),
                ('Ending', models.CharField(max_length=30)),
                ('Date', models.DateField(default=datetime.date.today)),
                ('Phone', models.IntegerField()),
                ('Type', models.CharField(max_length=30)),
            ],
        ),
    ]
