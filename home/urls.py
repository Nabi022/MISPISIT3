from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('horoscope/', views.horoscope, name='horoscope'),  # API для гороскопа
]
