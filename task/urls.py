from django.contrib import admin
from django.urls import path
from task import views
urlpatterns = [
    path('create/',views.create_todo),
    path('read/',views.read_data),
    path('update/<int:id>',views.update_todo),
]
