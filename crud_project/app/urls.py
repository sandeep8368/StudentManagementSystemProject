from django.urls import path
from app import views
urlpatterns = [
    path('add/', views.add, name='add'),
    path('update/', views.update, name= 'update'),
]
