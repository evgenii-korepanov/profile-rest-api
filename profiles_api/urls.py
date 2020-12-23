from django.urls import path
from profiles_api import views


urlpatterns = [
    path('HW-view/', views.HWApiView.as_view()),
]
