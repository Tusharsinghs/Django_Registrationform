
from django.urls import path, include

from .import views
urlpatterns = [
    path('login', views.Login, name='login'),
    path('register', views.Register, name='register'),
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout')

]
