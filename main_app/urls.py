from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name ='about'),
    path('ants/', views.ants_index, name='index'),
    path('ants/<int:ant_id>/', views.ants_detail, name='detail'),
    path('ants/create/', views.AntCreate.as_view(), name='ants_create'),
    path('ants/<int:pk>/update/', views.AntUpdate.as_view(), name='ants_update'),
    path('ants/<int:pk>/delete/', views.AntDelete.as_view(), name='ants_delete'),
    path('ants/<int:ant_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('ants/<int:antid>/assoc_food/<int:food_id>/', views.assoc_food, name='assoc_food'),
    path('ants/<int:ant_id>/unassoc_food/<int:food_id>/', views.unassoc_food, name='unassoc_food'),
    path('foods/', views.FoodList.as_view(), name='foods_index'),
    path('foods/<int:pk>/', views.FoodDetail.as_view(), name='foods_detail'),
    path('foods/create/', views.FoodCreate.as_view(), name='foods_create'),
    path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='foods_update'),
    path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),
]
