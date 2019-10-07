from django.urls import path
from . import views

app_name = 'declension'
urlpatterns = [
    path('', views.index, name="index"),
    path("<str:noun>", views.showDeclension, name="viewDeclension"),
    path("hello", views.hello, name="hello")
]