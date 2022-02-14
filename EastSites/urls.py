from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<str:cityName>/", views.city, name='city'),
    path("Site/<str:pk>/", views.site, name='site')
]