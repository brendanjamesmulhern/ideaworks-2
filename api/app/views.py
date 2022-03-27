from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .models import Course
from .models import Section
from .models import Lesson
from .serializers import UserSerializer, CourseSerializer, SectionSerializer, LessonSerializer
import bcrypt


# Routes for the API
@api_view(['GET'])
def index(request):
    urls = {
        'register user': '/api/users/register/',
        'login user': '/api/users/login/',
        'reset password': '/api/users/reset_password/<str:pk>/',
        'course search': '/api/courses/',
        'course get single': '/api/courses/course/<str:pk>/',
        'course create': '/api/courses/create/',
        'course update': '/api/courses/update/<str:pk>/',
        'course delete': '/api/courses/delete/<str:pk>/',
        'section search': '/api/sections/',
        'section get single': '/api/sections/section/<str:pk>/',
        'section create': '/api/sections/create/',
        'section update': '/api/sections/update/<str:pk>/',
        'section delete': '/api/sections/delete/<str:pk>/',
        'lesson search': '/api/lessons/',
        'lesson get single': '/api/lessons/lesson/<str:pk>/',
        'lesson create': '/api/lessons/create/',
        'lesson update': '/api/lessons/update/<str:pk>/',
        'lesson delete': '/api/lessons/delete/<str:pk>/',
    }
    return Response(urls)


# 'register user': '/api/users/register/'
@api_view(['POST'])
def register_user(request):
    hashed_password = bcrypt.hashpw(request.data['password'].encode('utf-8'), bcrypt.gensalt())
    print(hashed_password.decode('utf-8'))
    new_user = UserSerializer(data={
        'first_name': request.data['first_name'],
        'last_name': request.data['last_name'],
        'username': request.data['username'],
        'email': request.data['email'],
        'password': hashed_password.decode('utf-8'),
        'courses': [],
    })
    if new_user.is_valid():
        new_user.save()
        return Response(new_user.data)
    else:
        return Response(new_user.errors)


# 'login user': '/api/users/login/'
@api_view(['POST'])
def login_user(request):
    try:
        user = User.User.objects.get(username=request.data['username'])
        if bcrypt.checkpw(request.data['password'].encode('utf-8'), user.password.encode('utf-8')):
            return Response(UserSerializer(user).data)
        else:
            return Response({'error': 'Invalid password'})
    except User.User.DoesNotExist:
        return Response({'error': 'Invalid username'})


# 'course search': '/api/courses/'
@api_view(['GET'])
def course_search(request):
    courses = Course.Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


# 'course get single': '/api/courses/course/<str:pk>/'
@api_view(['GET'])
def course_get_single(request, pk):
    courses = Course.Course.objects.get(pk=pk)
    serializer = CourseSerializer(courses, many=False)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


# 'course create': '/api/courses/create/'
@api_view(['POST'])
def course_create(request):
    new_course = CourseSerializer(data=request.data)
    if new_course.is_valid():
        new_course.save()
        return Response(new_course.data)
    else:
        return Response(new_course.errors)


# 'course update': '/api/courses/update/<str:pk>/'
@api_view(['PUT'])
def course_update(request, pk):
    course = Course.Course.objects.get(pk=pk)
    updated_course = CourseSerializer(course, data=request.data)
    if updated_course.is_valid():
        updated_course.save()
        return Response(updated_course.data)
    else:
        return Response(updated_course.errors)


# 'course delete': '/api/courses/delete/<str:pk>/'
@api_view(['DELETE'])
def course_delete(request, pk):
    course = Course.Course.objects.get(pk=pk)
    course.delete()
    return Response("Course deleted")


# 'section search': '/api/sections/'
@api_view(['GET'])
def section_search(request):
    sections = Section.Section.objects.all()
    serializer = SectionSerializer(sections, many=True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


# 'section get single': '/api/sections/section/<str:pk>/'
@api_view(['GET'])
def section_get_single(request, pk):
    sections = Section.Section.objects.get(pk=pk)
    serializer = SectionSerializer(sections, many=False)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


# 'section create': '/api/sections/create/'
@api_view(['POST'])
def section_create(request):
    new_section = SectionSerializer(data=request.data)
    if new_section.is_valid():
        new_section.save()
        return Response(new_section.data)
    else:
        return Response(new_section.errors)


# 'section update': '/api/sections/update/<str:pk>/'
@api_view(['PUT'])
def section_update(request, pk):
    section = Section.Section.objects.get(pk=pk)
    updated_section = SectionSerializer(section, data=request.data)
    if updated_section.is_valid():
        updated_section.save()
        return Response(updated_section.data)
    else:
        return Response(updated_section.errors)

# 'section delete': '/api/sections/delete/<str:pk>/'
@api_view(['DELETE'])
def section_delete(request, pk):
    section = Section.Section.objects.get(pk=pk)
    section.delete()
    return Response("Section deleted")


# 'lesson search': '/api/lessons/'
@api_view(['GET'])
def lesson_search(request):
    lessons = Lesson.Lesson.objects.all()
    serializer = LessonSerializer(lessons, many=True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


# 'lesson get single': '/api/lessons/lesson/<str:pk>/'
@api_view(['GET'])
def lesson_get_single(reques, pk):
    lessons = Lesson.Lesson.objects.get(pk=pk)
    serializer = LessonSerializer(lessons, many=False)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


# 'lesson create': '/api/lessons/create/'
@api_view(['POST'])
def lesson_create(request):
    new_lesson = LessonSerializer(data=request.data)
    if new_lesson.is_valid():
        new_lesson.save()
        return Response(new_lesson.data)
    else:
        return Response(new_lesson.errors)


# 'lesson update': '/api/lessons/update/<str:pk>/'
@api_view(['PUT'])
def lesson_update(request, pk):
    lesson = Lesson.Lesson.objects.get(pk=pk)
    updated_lesson = LessonSerializer(lesson, data=request.data)
    if updated_lesson.is_valid():
        updated_lesson.save()
        return Response(updated_lesson.data)
    else:
        return Response(updated_lesson.errors)

# 'lesson delete': '/api/lessons/delete/<str:pk>/'
@api_view(['DELETE'])
def lesson_delete(request, pk):
    lesson = Lesson.Lesson.objects.get(pk=pk)
    lesson.delete()
    return Response("Lesson deleted")
