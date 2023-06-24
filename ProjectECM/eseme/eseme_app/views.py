from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render

from eseme_app.models import Course, Season, Members, Students

from rest_framework import filters

from eseme_app import filters as vfilters

from rest_framework import generics, status

from rest_framework.views import APIView

from rest_framework.response import Response

from eseme_app.serializers import CourseListSerializer, SeasonListSerializer, MembersListSerializer, StudentsListSerializer

# ----------------------------------------------------------------
# ----------------------- STUDENTS ---------------------------------
# ----------------------------------------------------------------

class StudentsGetByID(generics.ListAPIView):
    
    serializer_class = StudentsListSerializer
    queryset = Students.objects.all()
    
    filter_backends = [DjangoFilterBackend]
    
    filterset_class = vfilters.StudentByIdFilter
    
    # def get(self, request, id):
    #     try:
    #         #LOGICA
    #         movie = Students.objects.filter()
            
    #     except Students.DoesNotExist:
    #         return Response({'error': 'Not found'}, status = status.HTTP_404_NOT_FOUND)

    #     serializer = StudentsListSerializer(movie)
    #     return Response(serializer.data)    

# ----------------------------------------------------------------
# ----------------------- MEMBERS ---------------------------------
# ----------------------------------------------------------------

class MembersGetByDni(generics.ListAPIView):
    serializer_class = MembersListSerializer
    
    def get(self, request, dni):
        try:
            movie = Members.objects.get(memb_dni = dni)
        except Members.DoesNotExist:
            return Response({'error': 'Not found'}, status = status.HTTP_404_NOT_FOUND)

        serializer = MembersListSerializer(movie)
        
        return Response(serializer.data)

# ----------------------------------------------------------------
# ----------------------- COURSES ---------------------------------
# ----------------------------------------------------------------
    
class CourseList(generics.ListAPIView):
    serializer_class = CourseListSerializer

    def get_queryset(self):
        return Course.objects.all().order_by('cour_id')
    
class CourseDetailList(APIView):
    serializer_class = CourseListSerializer
    
    def get(self, request, pk):
        try:
            movie = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({'error': 'Not found'}, status = status.HTTP_404_NOT_FOUND)
 
        serializer = CourseListSerializer(movie)
        return Response(serializer.data)

# ----------------------------------------------------------------
# ----------------------- SEASON ---------------------------------
# ----------------------------------------------------------------
    
class SeasonList(generics.ListAPIView):
    serializer_class = SeasonListSerializer
    
    def get_queryset(self):
        
        #if request.method == 'GET' or request.method == 'OPTIONS':
        return Season.objects.all().order_by('seas_id')
    
    # def post(self, request):
    #     serializer = SeasonListSerializer(data=request.data)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
        
    #     else:
    #         return Response(serializer.errors)
        
class SeasonPost(generics.CreateAPIView):
    serializer_class = SeasonListSerializer
    
    def post(self, request):
        serializer = SeasonListSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)       
        
    
class SeasonDetailList(APIView):
    serializer_class = SeasonListSerializer
    
    def get(self, request, pk):
        try:
            movie = Season.objects.get(seas_id = pk)
        except Season.DoesNotExist:
            return Response({'error': 'Not found'}, status = status.HTTP_404_NOT_FOUND)

        serializer = SeasonListSerializer(movie)
        return Response(serializer.data)