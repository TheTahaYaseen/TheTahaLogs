from django.urls import path
from . import views

urlpatterns = [
    path("", views.logs_view, name="logs"),
    path("add", views.add_view, name="add_log"),
    path("update/<str:log_id>", views.update_view, name="update_log"),
    path("delete/<str:log_id>", views.delete_view, name="delete_log"),
]
