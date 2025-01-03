from django import forms
from .models import Course, Lesson
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .validators import *


class LessonForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': "Dars nomi",
        'class': 'form-control'
    }), label='Dars nomi', validators=[lesson_validator])
    teacher = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "O'qituvchi ismi",
        'class': 'form-control'
    }), label="O'qituvchi")
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "Dars haqida ma'lumot kiriting!",
        'class': 'form-control'
    }), label="Dars haqida", required=False)
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }), label='Rasmi', required=False)
    student_count = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': "Talabalar soni",
        'class': 'form-control'
    }), label='Talabalar soni', validators=[student_count_validator])
    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Dars narxi',
        'class': 'form-control'
    }), label='Dars narxi', validators=[price_validator])
    is_available = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'checked': 'checked'
    }), label="Qabul davom etyaptimi")
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={
        'class': 'form-select'
    }), label="Bog'langan kursi")

    def create(self):
        lesson = Lesson.objects.create(**self.cleaned_data)
        return lesson

    def update(self, lesson):
        lesson.name = self.cleaned_data.get('name')
        lesson.teacher = self.cleaned_data.get('teacher')
        lesson.description = self.cleaned_data.get('description')
        lesson.photo = self.cleaned_data.get('photo') if self.cleaned_data.get('photo') else lesson.photo
        lesson.student_count = self.cleaned_data.get('student_count')
        lesson.price = self.cleaned_data.get('price')
        lesson.is_available = self.cleaned_data.get('is_available')
        lesson.course = self.cleaned_data.get('course')
        lesson.save()


class CourseForm(forms.Form):
    name = forms.CharField(max_length=50, label='Kurs nomi', widget=forms.TextInput(attrs={
        'placeholder': 'Kurs nomini kiriting',
        'class': 'form-control'
    }), validators=[course_validator])

    def create(self):
        course = Course.objects.create(**self.cleaned_data)
        return course


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id': 'form3Example1cg',
        'class': 'form-control form-control-lg'
    }), validators=[username_validator, user_availibility_check])
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'form3Example3cg',
        'class': 'form-control form-control-lg'
    }), validators=[email_validator])
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'form3Example4cg',
        'class': 'form-control form-control-lg'
    }))
    password_confirm = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'form3Example4cdg',
        'class': 'form-control form-control-lg'
    }))

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password_confirm != password:
            raise ValidationError("Parollar bir xil bo'lishi kerak!")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id': 'typeEmailX-2',
        'class': 'form-control form-control-lg'
    }), validators=[login_validator])
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'typePasswordX-2',
        'class': 'form-control form-control-lg'
    }))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                password_check_by_username(username, password)
            except ValidationError as e:
                self.add_error('password', e.message)


class CommentForm(forms.Form):
    text = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 2,
    }), label='Izoh', validators=[comment_validator])

    def save(self, comment, user, lesson):
        comment.objects.create(
            text=self.cleaned_data.get('text'),
            author=user,
            lesson=lesson
        )

    def update(self, comment):
        comment.text = self.cleaned_data['text']
        comment.save()
