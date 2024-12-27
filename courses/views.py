from django.shortcuts import render, redirect
from .models import Course, Lesson
from .forms import LessonForm, CourseForm, RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


def home(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons': lessons,
        'title': 'Barcha kurs hamda darslar'
    }
    return render(request, 'index.html', context)


def lessons_by_courses(request, course_id):
    try:
        lessons = Lesson.objects.filter(course_id=course_id)
        course = Course.objects.get(pk=course_id)
        context = {
            'lessons': lessons,
            'title': f'{course.name}: barcha darslar '
        }
        return render(request, 'index.html', context)
    except:
        return render(request, '404.html', status=404)


def detail_lesson(request, lesson_id):
    try:
        lesson = Lesson.objects.get(pk=lesson_id)
        context = {
            'lesson': lesson,
            'title': lesson.description
        }
        return render(request, 'detail.html', context)
    except:
        return render(request, '404.html', status=404)


def add_lessons(request):
    if request.method == 'POST':
        form = LessonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            lesson = form.create()
            messages.success(request, "Dars muvaffaqiyatli tarzda qo'shildi")
            return redirect('detail_lesson', lesson_id=lesson.pk)

    form = LessonForm()
    context = {
        'form': form,
        'title': "Dars qo'shish"
    }
    return render(request, 'add_lesson.html', context)


def add_courses(request):
    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            course = form.create()
            messages.success(request, "Kurs muvaffaqiyatli tarzda qo'shildi!")
            return redirect('home')

    form = CourseForm()
    context = {
        'form': form,
        'title': "Kurs qo'shish"
    }

    return render(request, 'add_course.html', context)


def update_lesson(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)

    if request.method == 'POST':
        form = LessonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.update(lesson)
            messages.success(request, "Dars muvaffaqiyatli tarzda o'zgartirildi!")
            return redirect('detail_lesson', lesson_id=lesson.pk)

    form = LessonForm(initial={
        'name': lesson.name,
        'teacher': lesson.teacher,
        'description': lesson.description,
        'photo': lesson.photo,
        'student_count': lesson.student_count,
        'price': lesson.price,
        'is_available': lesson.is_available,
        'course': lesson.course
    })
    context = {
        'form': form,
        'photo': lesson.photo,
        'title': f"{lesson.name}: darsini tahrirlash!"
    }
    return render(request, 'add_lesson.html', context)


def delete_lesson(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.method == 'POST':
        lesson.delete()
        messages.success(request, "Dars muvaffaqiyatli tarzda o'chirildi!")
        return redirect('home')

    context = {
        'lesson': lesson,
        'title': f"{lesson.name}: darsini o'chirish!"
    }
    messages.warning(request, "Ushbu darsni o'chirmoqchimisiz?")
    return render(request, 'confirm_delete.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password_confirm = form.cleaned_data.get('password_confirm')
            if password == password_confirm:
                user = User.objects.create_user(
                    form.cleaned_data.get('username'),
                    form.cleaned_data.get('email'),
                    password
                )
                messages.success(request, "Foydalanuvchi muvaffaqiyatli tarzda kiritildi!")
                return redirect('login_view')
    context = {
        'form': RegisterForm(),
        'title': 'Sign Up Page'
    }
    return render(request, 'auth/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            messages.success(request, f"{username} web sahifamizga xush kelibsiz!")
            login(request, user)
            return redirect('home')
    context = {
        'form': LoginForm(),
        'title': 'Login Page'
    }
    return render(request, 'auth/login.html', context)


def logout_view(request):
    logout(request)
    messages.warning(request, "Siz sahifadan chiqib ketdingiz!")
    return redirect('login_view')
