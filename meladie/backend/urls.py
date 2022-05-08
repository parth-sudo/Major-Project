from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='backend/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='backend/logout.html'), name='logout'),
    path('analyze/', views.analyze, name='analyze'),
    path('predict/', views.heart_disease_prediction, name='prediction'),

    path('accounts/profile/', views.profile, name='profile'),
    path('predict_diabetes/', views.diabetes_prediction, name = 'diabetes_prediction'),

    path('information/heart_disease/', views.heart_disease_information, name = 'heart_disease_info'),
    path('information/diabetes/', views.diabetes_information, name = 'diabetes_info'),
    path('information/liver_disease/', views.liver_disease_information, name='liver_info'),
    path('consult_doctors/', views.consult_doctors, name='consult_doctors'),
    path('liver_prediction/', views.liver_prediction, name='liver_prediction'),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
