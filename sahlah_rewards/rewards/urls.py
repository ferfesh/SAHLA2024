from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, ProfitViewSet, ProfitRateViewSet

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'profits', ProfitViewSet)
router.register(r'profit-rates', ProfitRateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('network/', views.network, name='network'),
]
