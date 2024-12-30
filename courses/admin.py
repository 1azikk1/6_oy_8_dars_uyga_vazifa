from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Course, Lesson, Comment


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id',)
    list_editable = ('name',)
    actions_on_top = False
    actions_on_bottom = True
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Course, CourseAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher', 'starts_from', 'student_count', 'price', 'is_available', 'course', 'get_photo')
    list_display_links = ('id', 'name')
    list_editable = ('teacher', 'student_count', 'price', 'is_available')
    list_filter = ('name', 'teacher', 'is_available')
    actions_on_top = False
    actions_on_bottom = True
    search_fields = ('description',)

    def get_photo(self, lesson):
        if lesson.photo:
            return mark_safe(f'<img src="{lesson.photo.url}" width="200px">')
        return 'Rasm topilmadi!'

    get_photo.short_description = 'Rasmi'


admin.site.register(Lesson, LessonAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)

