# Generated by Django 4.0.3 on 2022-03-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_course_sections_section_articles_user_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='courses',
        ),
        migrations.AddField(
            model_name='user',
            name='bought_courses',
            field=models.ManyToManyField(related_name='bought_courses', to='app.course'),
        ),
        migrations.AddField(
            model_name='user',
            name='made_courses',
            field=models.ManyToManyField(related_name='made_courses', to='app.course'),
        ),
    ]
