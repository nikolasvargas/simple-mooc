from django.urls import path
from courses import views

app_name = 'courses'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.course, name='course')
]
