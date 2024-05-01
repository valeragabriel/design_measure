from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('user_page/', views.user_page, name='user_page'),
    path('services/', views.services, name='services'),
    path('bodyMeasure/', views.bodyMeasure, name='bodyMeasure'),
    path('clothMeasure/', views.clothMeasure, name='clothMeasure'),
    path('measureDate/', views.measureDate, name='measureDate'),
    path('user_services/', views.user_services, name='user_services'),
    path('results/', views.results, name='results'),

    ]