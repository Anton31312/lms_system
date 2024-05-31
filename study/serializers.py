from rest_framework import serializers

from study.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):


    class Meta:
        model = Lesson
        fields = '__all__' 


class CourseSerializer(serializers.ModelSerializer):

    count_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lesson(self, instance):
        if instance.lesson_set.all():
           return len(instance.lesson_set.all())
        return 0

       