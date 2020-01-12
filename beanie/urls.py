from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('<int:respocode>', views.respo_code, name="respo_code")
]
