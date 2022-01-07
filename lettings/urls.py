from django.urls import path

from lettings import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]

app_name = 'lettings'