# Generated by Django 2.1.1 on 2018-09-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0007_auto_20180922_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='value',
            field=models.IntegerField(verbose_name='Значение (в днях)'),
        ),
    ]
