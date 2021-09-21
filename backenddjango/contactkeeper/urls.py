from django.urls import path, include
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework import permissions

router = DefaultRouter()
router.register('contact', views.ContactViewSet)

urlpatterns = [
  path('', include(router.urls)),
]