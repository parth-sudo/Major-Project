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
 
    path('predict/', views.heart_disease_prediction, name='prediction'),

    path('accounts/profile/', views.profile, name='profile'),
    path('predict_diabetes/', views.diabetes_prediction, name = 'diabetes_prediction'),

    path('information/<str:disease_name>/', views.disease_information, name = 'disease_information'),
    path('consult_doctors/', views.consult_doctors, name='consult_doctors'),
    path('liver_prediction/', views.liver_prediction, name='liver_prediction'),

    path('analyze/<str:parameter>/', views.analyze1, name='analyze'),
    path('bookLabTests', views.book_lab_test, name = 'book_lab_test'),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
