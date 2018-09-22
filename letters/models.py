from django.db import models

# Create your models here.
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Letter(models.Model):
    title           =   models.CharField(max_length=220)
    text_content    =   models.TextField(
                            'Текст письма подтверждения регистрации в формате "text"',
                            blank = True, null = True, default = None,
                        )
    html_content    =   models.TextField(
                            'Текст письма подтверждения регистрации в формате "html"',
                            blank = True, null = True, default = None,
                        )
    # html_content    = RichTextUploadingField( 'Текст письма подтверждения регистрации в формате "text"', )
    featured        =   models.BooleanField(default=False)


    class Meta:
            ordering            = ( 'title', )
            verbose_name        = 'Шаблон письма подтверждения аккаунта по email'
            verbose_name_plural = 'Шаблоны писем подтверждения аккаунта по email'


    def save(self, *args, **kwargs):
        if self.featured:
            qs = Letter.objects.filter(featured=True).exclude(pk=self.pk)
            if qs.exists():
                qs.update(featured=False)
        super(Letter, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

class Setting(models.Model):
    name = models.CharField('Название', max_length=100)
    value = models.IntegerField('Значение (в днях)')
    class Meta:
            ordering            = ( 'name', )
            verbose_name        = 'Настройка'
            verbose_name_plural = 'Настройки'

    def __str__(self):
        return self.name