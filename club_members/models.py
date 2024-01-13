from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
from slugify import slugify


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    header = models.TextField(max_length=64, blank=True, verbose_name="Заголовок")
    description = models.TextField(max_length=2000, blank=True, verbose_name="Описание")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")

    def __str__(self):
        return f"{self.user.username} - {self.id}"

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    date_posted = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-date_posted']

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    pdf_data = models.BinaryField(verbose_name="PDF Файл")

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) if self.title else "document"
        super(Document, self).save(*args, **kwargs)

