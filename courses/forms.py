from django import forms
from .models import Course


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


class CourseForm(forms.Form):
    name = forms.CharField(max_length=50, label='Kurs nomi', widget=forms.TextInput(attrs={
        'placeholder': 'Kurs nomini kiriting',
        'class': 'form-control'
    }))
