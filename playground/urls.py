from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'usermodels',UserViewSet)

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('',include(router.urls)),
]
