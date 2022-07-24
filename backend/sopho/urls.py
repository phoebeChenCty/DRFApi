from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()
router.register('', views.CakeViewSet, basename='cakes')

urlpatterns = [
    path('bigmelon/changefruit', views.ChangeFruitView.as_view()),
    path('bigmelon/gameover', views.GameOverView.as_view()),
    path('bigmelon/nono', views.GameOverNoNoView.as_view(), name='nono'),
    path('bigmelon/order', views.GameOverOrderView.as_view(), name='order'),
    # http://192.168.254.125:8000/sopho/cakes/1/
    path('cakes/', include(router.urls))
]
