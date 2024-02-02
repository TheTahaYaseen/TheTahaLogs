from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("authentication", include("authentication.urls")),
    path("log", include("log.urls")),
]
