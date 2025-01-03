from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Lesson, Comment
from .forms import LessonForm, CourseForm, RegisterForm, LoginForm, CommentForm
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
            'title': lesson.description,
            'form': CommentForm(),
            'comments': Comment.objects.filter(lesson_id=lesson_id)
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

    else:
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
    else:
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
    else:
        form = RegisterForm()
    context = {
        'form': form,
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
    else:
        form = LoginForm()
    context = {
        'form': form,
        'title': 'Login Page'
    }
    return render(request, 'auth/login.html', context)


def logout_view(request):
    logout(request)
    messages.warning(request, "Siz sahifadan chiqib ketdingiz!")
    return redirect('login_view')


def comment_save(request, lesson_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            if form.is_valid():
                lesson = get_object_or_404(Lesson, pk=lesson_id)
                Comment.objects.create(
                    text=form.cleaned_data.get('text'),
                    author=request.user,
                    lesson=lesson
                )
                messages.success(request, "Izoh qo'shildi!")
            else:
                messages.error(request, "Izoh uchun matn berilgan miqdordan oshib ketdi!")

        return redirect('detail_lesson', lesson_id=lesson_id)
    messages.error(request, "Izoh qo'shish uchun avval saytga kiring!!!")
    return redirect('login_view')


def delete_comment(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.user == comment.author or request.user.is_superuser:
            lesson = comment.lesson.pk
            comment.delete()
            messages.success(request, "Izoh o'chirildi!")
            return redirect('detail_lesson', lesson_id=lesson)

        messages.error(request, "Izohni o'chirsh uchun avval login qiling!")
        return redirect('login_view')


def comment_update(request, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_id)
        lesson_id = comment.lesson.id

        if request.user == comment.author or request.user.is_superuser:
            if request.method == 'POST':
                form = CommentForm(data=request.POST)
                if form.is_valid():
                    form.update(comment)
                    messages.success(request, "Izoh muvaffaqiyatli o'zgartirildi.")
                    return redirect('detail_lesson', lesson_id=lesson_id)

            else:
                form = CommentForm(initial={'text': comment.text})

            context = {
                'lesson': comment.lesson,
                'form': form,
                'update': True,
                'comments': Comment.objects.filter(pk=comment_id)
            }
            return render(request, 'detail.html', context)

    else:
        messages.error(request, "Avval syatga kirishingiz kerak!")
        return redirect('login_view')

