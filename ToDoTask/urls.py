from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('NewTask/', views.newtask, name='newtask'),
    path('Complete/<str:pk>', views.complete, name='complete'),
    path('Delete/<str:pk>', views.delete_task, name='delete'),
]
