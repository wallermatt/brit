from django.urls import path

from . import views

urlpatterns = [
    path('detail', views.detail, name='detail'),
    path('summary', views.summary, name='summary'),
]
