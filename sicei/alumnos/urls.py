from django.urls import path
from .views import alumnoView
from . import views

urlpatterns = [
    path('', alumnoView.as_view(), name='alumno-list'),
    path('<int:pk>/', alumnoView.as_view(), name='alumno-detail'),
]