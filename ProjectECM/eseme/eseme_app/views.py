from django.shortcuts import get_object_or_404

from django.shortcuts import render

from eseme_app.models import Course, Season

from rest_framework import generics, status

from rest_framework.views import APIView

from rest_framework.response import Response

from eseme_app.serializers import CourseListSerializer, SeasonListSerializer
    
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
            movie = Season.objects.get(pk=pk)
        except Season.DoesNotExist:
            return Response({'error': 'Not found'}, status = status.HTTP_404_NOT_FOUND)

        serializer = SeasonListSerializer(movie)
        return Response(serializer.data)