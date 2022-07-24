from django.urls import path

from . import views

urlpatterns = [
    path('bigmelon/changefruit', views.ChangeFruitView.as_view()),
    path('bigmelon/gameover', views.GameOverView.as_view()),
    path('bigmelon/nono', views.GameOverNoNoView.as_view(), name='nono'),
    path('bigmelon/order', views.GameOverOrderView.as_view(), name='order'),
]
