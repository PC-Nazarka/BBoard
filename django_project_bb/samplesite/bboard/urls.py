from django.urls import path
from . import views

app_name = 'bboard'
urlpatterns = [
    path('add/', views.CreateItem.as_view(), name='add'),
    path('<int:rubric_id>/', views.RenderByRubric.as_view(), name='by_rubric'),
    path('', views.MainPage.as_view(), name='index'),
    path('item_bb_<int:pk>', views.NewItemPage.as_view(), name="page"),
    path('item_bb_<int:pk>/update', views.ItemUpdate.as_view(), name="page_update"),
    path('item_bb_<int:pk>/delete', views.ItemDelete.as_view(), name="page_delete"),
    path('search/', views.SearchResults.as_view(), name='search')
]