from django.urls import path
from .views import cars_list, car_detail, car_create, car_update, car_delete

urlpatterns = [
    path('cars/', cars_list),
    path('cars/<int:pk>/', car_detail),
    path('cars/create/', car_create),
    path('cars/update/<int:pk>/', car_update),
    path('cars/delete/<int:pk>/', car_delete)
  
]