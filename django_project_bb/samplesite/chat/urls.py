from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.HomeChat.as_view(), name='chat'),
    path('id<int:pk>/', views.RoomChat.as_view(), name='room'),
]