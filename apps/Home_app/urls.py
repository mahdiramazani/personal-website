from django.urls import path
from apps.Home_app import views

app_name="Home_app"
urlpatterns=[
    path("",views.HomeView.as_view(),name="Home")
]