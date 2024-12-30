from django.urls import path
from .views import (home, lessons_by_courses, detail_lesson, add_lessons, add_courses, update_lesson, delete_lesson,
                    register, login_view, logout_view, comment_save, delete_comment, comment_update)

urlpatterns = [
    path('', home, name='home'),
    path('courses/<int:course_id>/', lessons_by_courses, name='lessons_by_courses'),
    path('lesson/<int:lesson_id>/', detail_lesson, name='detail_lesson'),
    path('lesson/<int:lesson_id>/update/', update_lesson, name='update_lesson'),
    path('lesson/<int:lesson_id>/delete/', delete_lesson, name='delete_lesson'),
    path('lessons/add/', add_lessons, name='add_lessons'),
    path('courses/add/', add_courses, name='add_courses'),

    path('lessons/<int:lesson_id>/comment/save/', comment_save, name='comment_save'),
    path('lesson/comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    path('lesson/comment/<int:comment_id>/update/', comment_update, name='comment_update'),

    path('register/', register, name='register'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
]
