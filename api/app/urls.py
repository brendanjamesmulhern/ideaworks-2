from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('users/register/', views.register_user),
    path('users/login/', views.login_user),
    path('users/reset_password/<str:pk>/', auth_views.PasswordChangeView.as_view()),
    path('courses/', views.course_search),
    path('courses/course/<str:pk>/', views.course_get_single),
    path('courses/create/', views.course_create),
    path('courses/update/<str:pk>/', views.course_update),
    path('courses/delete/<str:pk>/', views.course_delete),
    path('sections/', views.section_search),
    path('sections/section/<str:pk>/', views.section_get_single),
    path('sections/create/', views.section_create),
    path('sections/update/<str:pk>/', views.section_update),
    path('sections/delete/<str:pk>/', views.section_delete),
    path('lessons/', views.lesson_search),
    path('lessons/lesson/<str:pk>/', views.lesson_get_single),
    path('lessons/create/', views.lesson_create),
    path('lessons/update/<str:pk>/', views.lesson_update),
    path('lessons/delete/<str:pk>/', views.lesson_delete),
]