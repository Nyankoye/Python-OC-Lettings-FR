from django.urls import path

from profiles import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]

app_name='profiles'