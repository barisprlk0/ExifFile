from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.index, name='image_upload'),

]