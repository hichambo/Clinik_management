from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views  # Assuming your views are in the same directory

router = DefaultRouter()
router.register(r'diet-plans', views.DietPlanViewSet, basename='dietplan')

urlpatterns = router.urls
