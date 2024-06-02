from django.urls import path, include
from django.contrib import admin
from . import views
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, ProfitViewSet, ProfitRateViewSet

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'profits', ProfitViewSet)
router.register(r'profit-rates', ProfitRateViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('network/', views.network, name='network'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
