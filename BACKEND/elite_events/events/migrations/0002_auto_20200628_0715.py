# Generated by Django 3.0.7 on 2020-06-28 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decoration',
            name='status',
            field=models.CharField(default='Active', max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(default='Active', max_length=50),
        ),
        migrations.AlterField(
            model_name='photography',
            name='status',
            field=models.CharField(default='Active', max_length=20),
        ),
        migrations.AlterField(
            model_name='venues',
            name='status',
            field=models.CharField(default='Active', max_length=20),
        ),
    ]