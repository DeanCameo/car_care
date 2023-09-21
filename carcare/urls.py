from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing_page'),
    path('home/', views.home, name='home'),
    path('cars/', views.cars, name='cars_home'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('create_car/', views.create_car, name='create_car'),
    path('car/<int:car_id>/', views.car_details, name='car_details'),
    path('car/<int:car_id>/service_history/', views.service_history, name='service_history'),
    path('car/<int:car_id>/repair_history/', views.repair_history, name='repair_history'),
    path('car/<int:car_id>/wheel_change_history/', views.wheel_change_history, name='wheel_change_history'),
    path('car/<int:car_id>/insurance_history/', views.insurance_history, name='insurance_history'),
    path('car/<int:car_id>/fuel_history/', views.fuel_history, name='fuel_history'),
    path('car/<int:car_id>/create_service/', views.create_service, name='create_service'),
    path('car/<int:car_id>/create_repair/', views.create_repair, name='create_repair'),
    path('car/<int:car_id>/create_wheel_change/', views.create_wheel_change, name='create_wheel_change'),
    path('car/<int:car_id>/create_insurance/', views.create_insurance, name='create_insurance'),
    path('car/<int:car_id>/create_fuel/', views.create_fuel, name='create_fuel'),
]