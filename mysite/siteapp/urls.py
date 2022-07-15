from django.urls import path
from . import views
urlpatterns=[
    path('',views.OpenHOME),
    path('login',views.LoginDetails),
    path('form',views.Form)
]