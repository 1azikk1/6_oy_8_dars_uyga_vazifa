# Generated by Django 5.1.3 on 2024-12-29 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created'], 'verbose_name': 'fikr ', 'verbose_name_plural': 'fikrlar'},
        ),
    ]