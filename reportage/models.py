from django.db import models
from account.models import User
from category.models import Category
# Create your models here.


class Reportage(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reportages')
    image_1 = models.ImageField(upload_to='reportage/images')
    image_2 = models.ImageField(upload_to='reportage/images', blank=True)
    image_3 = models.ImageField(upload_to='reportage/images', blank=True)
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(
        Category, blank=True, related_name='reportages')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(
        User, blank=True, related_name='dislikes')
    score = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title[0:20]

    class Meta:
        verbose_name = 'گزارش'
        verbose_name_plural = '  گزارش ها'

    def likes_count(self):
        return self.likes.count()

    def dislike_count(self):
        return self.dislikes.count()

    def images_count(self):
        if self.image_3:
            return "012"
        if self.image_2:
            return "01"
        if self.image_1:
            return "0"
