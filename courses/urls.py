from django.urls import path
from .views import home, lessons_by_courses, detail_lesson, add_lessons, add_courses

urlpatterns = [
    path('', home, name='home'),
    path('courses/<int:course_id>/', lessons_by_courses, name='lessons_by_courses'),
    path('lesson/<int:lesson_id>/', detail_lesson, name='detail_lesson'),
    path('lessons/add/', add_lessons, name='add_lessons'),
    path('courses/add/', add_courses, name='add_courses'),
]
