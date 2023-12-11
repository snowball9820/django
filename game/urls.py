from django.urls import path
from . import views

urlpatterns = [
    path("", views.gamepage, name="gamepage"),
    path("fortest", views.fortest, name="fortest"),
    path("datatest", views.datatest, name="datatest"),
    path("mediatest", views.mediatest, name="mediatest"),
    path("threadtest", views.threadtest, name="threadtest")
]