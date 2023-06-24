from rest_framework import serializers
from eseme_app.models import Course, Season, Members, Students

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class SeasonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"        

class MembersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = "__all__"        

class StudentsListSerializer(serializers.ModelSerializer):
    
    student_name = serializers.CharField(read_only=True, source='stud_member.memb_name') 
    course_name = serializers.CharField(read_only=True, source='stud_season.seas_course.cour_description')
    teacher_name = serializers.CharField(read_only=True, source='stud_season.seas_teacher')
    #season_mode = serializers.CharField(read_only=True, source='stud_season.seas_mode')
    dni = serializers.CharField(read_only=True, source='stud_member.memb_dni')  
    
    #stud_season__seas_teacher__memb_name = serializers.CharField(read_only=True, source='stud_season.seas_teacher.memb_name') 
    #stud_season__seas_course__cour_description = serializers.CharField(read_only=True, source='stud_season.seas_course.cour_description') 
    #stud_season__seas_course__cour_level = serializers.CharField(read_only=True, source='stud_season.seas_course.cour_level') 
    #pais_destino__descripcion = serializers.CharField(read_only=True, source='pais_destino.descripcion')
    
    class Meta:
        model = Students
        fields = ['student_name', 'course_name', 'teacher_name', 'seas_final','dni'] 