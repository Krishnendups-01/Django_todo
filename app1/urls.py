from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('delete<int:id>',views.delete, name='delete'),
    path('items',views.Todoitems, name = 'items'),
    
]