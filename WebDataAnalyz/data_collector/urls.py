from django.urls import path

from . import views

urlpatterns = [
    path("run-crawler/", views.run_crawler, name="run_crawler"),
]
