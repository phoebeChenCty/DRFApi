from django.urls import path

from . import views

urlpatterns = [
    path('bigmelon/changefruit', views.ChangeFruitView.as_view())
]
