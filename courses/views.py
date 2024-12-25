from django.shortcuts import render, redirect
from .models import Course, Lesson
from .forms import LessonForm, CourseForm
from django.contrib import messages


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
            lesson = Lesson.objects.create(**form.cleaned_data)
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
            course = Course.objects.create(**form.cleaned_data)
            print(course, "qo'shildi!")

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
            lesson.name = form.cleaned_data.get('name')
            lesson.teacher = form.cleaned_data.get('teacher')
            lesson.description = form.cleaned_data.get('description')
            lesson.photo = form.cleaned_data.get('photo') if form.cleaned_data.get('photo') else lesson.photo
            lesson.student_count = form.cleaned_data.get('student_count')
            lesson.price = form.cleaned_data.get('price')
            lesson.is_available = form.cleaned_data.get('is_available')
            lesson.course = form.cleaned_data.get('course')
            lesson.save()
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
    }
    return render(request, 'add_lesson.html', context)


def delete_lesson(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    if request.method == 'POST':
        lesson.delete()
        messages.success(request, "Dars muvaffaqiyatli tarzda o'chirildi!")
        return redirect('home')

    context = {
        'lesson': lesson
    }
    messages.warning(request, "Ushbu darsni o'chirmoqchimisiz?")
    return render(request, 'confirm_delete.html', context)
