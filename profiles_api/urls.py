from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hw-viewset', views.HWViewSet, base_name='hw-viewset')


urlpatterns = [
    path('HW-view/', views.HWApiView.as_view()),
    path('', include(router.urls)),
]
