from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = "index"),
    path('data/', views.data, name = "data")
]