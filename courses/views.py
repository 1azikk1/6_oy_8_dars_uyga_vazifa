from django.shortcuts import render
from .models import Course, Lesson
from .forms import LessonForm, CourseForm


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
            print(lesson, "qo'shildi!")

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
