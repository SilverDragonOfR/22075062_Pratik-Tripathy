from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("list", views.list, name="list"),
    path("find/<str:shortURL>", views.go, name="go"),
]
