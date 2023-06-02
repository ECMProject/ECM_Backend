from django.urls import path, include

from eseme_app import views

urlpatterns = [
    path('courses/', views.CourseList.as_view(), name='courses'),
    path('courses/<int:pk>/', views.CourseDetailList.as_view(), name='courses_detail'),
]
