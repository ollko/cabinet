# Generated by Django 2.1.1 on 2018-09-15 08:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0002_auto_20180915_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст письма подтверждения регистрации'),
        ),
    ]
