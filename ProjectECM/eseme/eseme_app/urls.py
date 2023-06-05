from django.urls import path, include

from eseme_app import views

urlpatterns = [
    path('courses/', views.CourseList.as_view(), name='courses'),
    path('courses/<int:pk>/', views.CourseDetailList.as_view(), name='courses_detail'),
    path('season/', views.SeasonList.as_view(), name='season'),
    path('season/post', views.SeasonPost.as_view(), name='season_post'),
    path('season/<int:pk>/', views.SeasonDetailList.as_view(), name='season_detail'),
]
