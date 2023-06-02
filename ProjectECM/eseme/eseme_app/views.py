from django.shortcuts import render

from eseme_app.models import Course

from rest_framework import generics, status

from rest_framework.views import APIView

from rest_framework.response import Response

from eseme_app import serializers
    
class CourseList(generics.ListAPIView):
    serializer_class = serializers.CourseListSerializer

    def get_queryset(self):
        return Course.objects.all().order_by('cour_id')
    
class CourseDetailList(APIView):
    serializer_class = serializers.CourseListSerializer
    
    def get(self, request, pk):
        try:
            movie = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({'error': 'Not found'}, status = status.HTTP_404_NOT_FOUND)

        serializer = serializers.CourseListSerializer(movie)
        return Response(serializer.data)        