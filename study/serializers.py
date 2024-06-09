from rest_framework import serializers

from study.models import Course, Lesson, Subscribe
from study.validators import SiteValidatior


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = '__all__' 


class LessonSerializer(serializers.ModelSerializer):


    class Meta:
        model = Lesson
        fields = '__all__' 
        validators = [SiteValidatior(url='url_link')]


class CourseSerializer(serializers.ModelSerializer):

    count_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lesson(self, instance):
        if instance.lesson_set.all():
           return instance.lesson_set.count()
        return 0
       
    def get_subscribe(self, instance):
        user = self.context['request'].user
        return Subscribe.objects.filter(user=user, course=instance).exists()