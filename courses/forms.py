from django import forms
from .models import Course, Lesson


class LessonForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': "Dars nomi",
        'class': 'form-control'
    }), label='Dars nomi')
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
    }), label='Talabalar soni')
    price = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Dars narxi',
        'class': 'form-control'
    }), label='Dars narxi')
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
    }))

    def create(self):
        course = Course.objects.create(**self.cleaned_data)
        return course


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id': 'form3Example1cg',
        'class': 'form-control form-control-lg'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'form3Example3cg',
        'class': 'form-control form-control-lg'
    }))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'form3Example4cg',
        'class': 'form-control form-control-lg'
    }))
    password_confirm = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'form3Example4cdg',
        'class': 'form-control form-control-lg'
    }))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id': 'typeEmailX-2',
        'class': 'form-control form-control-lg'
    }))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'typePasswordX-2',
        'class': 'form-control form-control-lg'
    }))
