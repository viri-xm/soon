from django.urls import path
from . import views

urlpatterns = [
    path('soon', views.index, name='soon'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
]
