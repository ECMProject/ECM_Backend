from rest_framework import serializers
from eseme_app.models import Course, Season

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class SeasonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"        
