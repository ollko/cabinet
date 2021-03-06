# Generated by Django 2.1.1 on 2018-09-20 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_auto_20180919_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lisence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, default='XXXX-XXXX-XXXX-XXXX', max_length=19, verbose_name='Номер лицензии')),
                ('hwid', models.CharField(blank=True, default='HHHHH-HHHHH-HHHHH-HHHHH', max_length=23, verbose_name='hwid оборудования')),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='Время начала')),
                ('end', models.DateTimeField(auto_now_add=True, verbose_name='Время окончания')),
                ('user_payments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_lisence', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AlterField(
            model_name='payment',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='for_what_product', to='shop.Product', verbose_name='За что платим'),
        ),
    ]
