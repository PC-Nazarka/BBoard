from django.urls import path
from . import views

urlpatterns = [
    path('id<int:pk>/', views.ProfileView.as_view(), name='user_profile'),
    path('id<int:pk>/update/', views.UpdateUserProfile.as_view(), name='user_profile_update'),
]
