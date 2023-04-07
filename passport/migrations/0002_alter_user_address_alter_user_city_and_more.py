# Generated by Django 4.2 on 2023-04-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес проживания'),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Город проживания'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='number_of_phone',
            field=models.IntegerField(blank=True, max_length=11, null=True, verbose_name='Номер телфона'),
        ),
    ]
