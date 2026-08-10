from django.urls import path
from . import views

app_name = 'simulator'

urlpatterns = [
    path('airports/', views.airport_list, name='airport_list'),
    path('airports/create/',views.airport_create, name="airport_create"),
    path('airports/update/', views.airport_update, name='airport_update'),
    path("airport/delete/", views.airport_delete, name= 'airport_delete')
]