from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import *


# username validators
def username_validator(value):
    if ' ' in value:
        raise ValidationError("Foydalanuchi nomi bo'sh joylarsiz yozilishi kerak!")


def user_availibility_check(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError("Ushbu foydalanuvchi nomi bilan ro'yhatdan o'tilgan!")


# email validator
def email_validator(value: str):
    if not value.endswith('.com'):
        raise ValidationError('Email kiritishda xatolik yuz berdi!')


# course and lesson names
def lesson_validator(value):
    if Lesson.objects.filter(name=value).exists():
        raise ValidationError("Bunday dars mavjud!")


def course_validator(value):
    if Course.objects.filter(name=value).exists():
        raise ValidationError("Bunday kurs mavjud!")


# login validator
def login_validator(value):
    if not User.objects.filter(username=value).exists():
        raise ValidationError("Bunday foydalanuvchi mavjud emas!")


# comment text length
def comment_validator(value):
    if len(value) > 1000:
        raise ValidationError("Izoh matni miqdordan oshib ketdi!")


# student count validator
def student_count_validator(value):
    if value < 0:
        raise ValidationError("Talabalar sonini ifodalash uchun musbat son kiriting!")


# price validator
def price_validator(value):
    if value < 0:
        raise ValidationError("Narxni kiritishda musbat sondan foydalaning!")


# password check by username
def password_check_by_username(username, password):
    user = User.objects.get(username=username)
    if not check_password(password, user.password):
        raise ValidationError("Noto'g'ri parol kiritildi!")
