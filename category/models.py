from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name
