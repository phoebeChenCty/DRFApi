from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.ProductViewSet, basename='products')

# urlpatterns = [
#     path('', views.product_mixin_view),
#     path('<int:pk>/update/', views.product_update_view),
#     path('<int:pk>/delete/', views.product_destroy_view),
#     path('<int:pk>/', views.product_mixin_view)  # pk: primary key
# ]

urlpatterns = [
    path('', include(router.urls))
]
