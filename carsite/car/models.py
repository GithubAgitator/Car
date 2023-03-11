
from django.db import models



# Create your models here.

class Car(models.Model):
    
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Характеристика")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография")
    cena = models.TextField(blank=True, verbose_name="Цена")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Военная техника'
        verbose_name_plural = 'Военная техника'


