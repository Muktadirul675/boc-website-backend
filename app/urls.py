from django.urls import path
from . import views

app_name = 'boc'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name='contact'),
    path('sign_up/', views.sign_up,name="sign_up"),
    path('sign_in/',views.sign_in, name="sign_in"),
    path('logout/', views.sign_out, name="log_out"),
    path('profile/', views.profile, name='profile'),
]