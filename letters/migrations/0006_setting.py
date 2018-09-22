# Generated by Django 2.1.1 on 2018-09-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0005_auto_20180921_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('value', models.IntegerField(verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
                'ordering': ('name',),
            },
        ),
    ]