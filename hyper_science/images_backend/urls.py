from django.urls import path

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from images_backend import views

router = DefaultRouter()

urlpatterns = [
    path('persons/', views.ListCreateAPIPersonView.as_view(), name='person-list'),
    path('persons/<uuid:pk>/', views.RetrieveUpdateDestroyAPIPersonView.as_view(), name='person-update')
]