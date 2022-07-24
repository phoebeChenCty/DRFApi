from django.urls import path

from . import views

urlpatterns = [
    path('bigmelon/changefruit', views.ChangeFruitView.as_view()),
    path('bigmelon/gameover', views.GameOverView.as_view())
]
