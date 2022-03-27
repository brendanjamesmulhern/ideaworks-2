from rest_framework.serializers import ModelSerializer
from .models import User
from .models import Course 
from .models import Section
from .models import Lesson


class UserSerializer(ModelSerializer):
    class Meta:
        model = User.User
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course.Course
        fields = '__all__'


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section.Section
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson.Lesson
        fields = '__all__'
