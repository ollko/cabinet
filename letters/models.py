from django.db import models

# Create your models here.
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Letter(models.Model):
    title       = models.CharField(max_length=220)
    content     = RichTextUploadingField( 'Текст письма подтверждения регистрации', )
    featured    = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if self.featured:
            qs = Letter.objects.filter(featured=True).exclude(pk=self.pk)
            if qs.exists():
                qs.update(featured=False)
        super(Letter, self).save(*args, **kwargs)


    def __str__(self):
        return self.title