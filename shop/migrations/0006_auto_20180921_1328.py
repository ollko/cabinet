# Generated by Django 2.1.1 on 2018-09-21 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20180921_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lisence',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_lisences', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
