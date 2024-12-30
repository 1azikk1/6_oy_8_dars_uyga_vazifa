from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Course(models.Model):
    objects = None
    name = models.CharField(max_length=50, unique=True, verbose_name='Kurs nomi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqit")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'kurs '
        verbose_name_plural = 'kurslar'


class Lesson(models.Model):
    objects = None
    name = models.CharField(max_length=50, verbose_name='Dars nomi')
    teacher = models.CharField(max_length=100, verbose_name="O'qituvchi ismi")
    description = models.TextField(null=True, blank=True, verbose_name='Dars haqida')
    starts_from = models.DateTimeField(default=datetime(2024, 1, 1, 8, 0), verbose_name='Boshlanish vaqti')
    photo = models.ImageField(upload_to='lessons/photos', blank=True, null=True)
    student_count = models.IntegerField(verbose_name='Talabalar soni')
    price = models.IntegerField(verbose_name='narxi')
    is_available = models.BooleanField(default=True, verbose_name='bor yoki yoq')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Bog'langan kurs")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'dars '
        verbose_name_plural = 'darslar'
        ordering = ('-starts_from',)


class Comment(models.Model):
    text = models.CharField(max_length=1000, verbose_name="Matni")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}|{self.text[:20]}|{self.lesson.name}"

    class Meta:
        verbose_name = 'fikr '
        verbose_name_plural = 'fikrlar'
        ordering = ['-created']
