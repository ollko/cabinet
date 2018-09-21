from django.utils import timezone


from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

PERIODS =   (
                ('1 месяц', '1 месяц',),
                ('3 месяца', '3 месяца',),
                ('6 месяцев', '6 месяцев',),
                ('12 месяцев', '12 месяцев',),
            )
class Lisence(models.Model):
    number  =   models.CharField(
                    'Номер лицензии',
                    max_length = 19,
                    blank = True,
                    default = 'XXXX-XXXX-XXXX-XXXX',
                )
    hwid    =   models.CharField(
                    'hwid оборудования',
                    max_length = 23,
                    blank = True,
                    default = 'HHHHH-HHHHH-HHHHH-HHHHH',
                )
    user = models.ForeignKey(
                        User,
                        verbose_name = 'Пользователь',
                        related_name = 'user_lisences',
                        on_delete    =  models.CASCADE,
                        )
    start   =   models.DateTimeField(
                    verbose_name='Время начала',
                    auto_now_add=True,
                )
    end     =   models.DateTimeField(
                    verbose_name='Время окончания',
                )

    class Meta:
        ordering            = ('end', )
        verbose_name        = 'Лицензия'
        verbose_name_plural = 'Лицензии'


    def __str__(self):
        return self.number


    def is_active(self):
        if self.end > timezone.now():
            return 'активна'
        return 'не активна'




class Product(models.Model):
    name = models.CharField('Период подписки', choices = PERIODS, max_length = 12)
    price  = models.DecimalField('Цена', max_digits=10, decimal_places=2,)


    def __str__(self):
        return self.name
    class Meta:
        ordering            = ('name', )
        verbose_name        = 'Продукт'
        verbose_name_plural = 'Продукты'


class Payment(models.Model):
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=u"Сумма платежа",
        default = 1000.00,
    )
    user    = models.ForeignKey(
        User,
        verbose_name = 'Платильщик',
        related_name='user_payments',
        on_delete=models.SET_NULL,
        null=True,
    )
    created = models.DateTimeField(
        verbose_name='Дата платежа',
        auto_now_add=True,)


    class Meta:
        ordering            = ('-created', )
        verbose_name        = 'Платеж'
        verbose_name_plural = 'Платежы'


    def __str__(self):
        return self.created.strftime("%Y-%m-%d %H:%M:%S %Z")