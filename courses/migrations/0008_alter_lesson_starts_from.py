# Generated by Django 5.1.3 on 2024-12-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_lesson_starts_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='starts_from',
            field=models.DateTimeField(default='2024, 1, 1, 08, 00', verbose_name='Boshlanish vaqti'),
        ),
    ]
