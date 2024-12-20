from django.shortcuts import render
from .models import Course, Lesson


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
