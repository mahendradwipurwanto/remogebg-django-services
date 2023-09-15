from django.urls import path
from . import views

urlpatterns = [
    path('remove-bg', views.remove_background, name='remove_background'),
]
