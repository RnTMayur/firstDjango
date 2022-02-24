from django.contrib import admin
from django.urls import path,include
from livesite import views
urlpatterns = [
    path('index',views.index,name="index"),
    path('insert',views.insert,name="insert"),
    path('delete',views.delete,name="delete"),
    path('edit',views.edit,name="edit"),
    path('edited',views.edited,name="edited"),
]
