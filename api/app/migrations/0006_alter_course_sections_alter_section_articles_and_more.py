# Generated by Django 4.0.3 on 2022-03-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_user_courses_user_bought_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='sections',
            field=models.ManyToManyField(blank=True, null=True, related_name='courses', to='app.section'),
        ),
        migrations.AlterField(
            model_name='section',
            name='articles',
            field=models.ManyToManyField(blank=True, null=True, related_name='sections', to='app.lesson'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bought_courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='bought_courses', to='app.course'),
        ),
        migrations.AlterField(
            model_name='user',
            name='made_courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='made_courses', to='app.course'),
        ),
    ]
