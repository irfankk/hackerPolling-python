from django.conf.urls import url, include

from rest_framework import routers

from apis.identity import views

router = routers.DefaultRouter()
router.register(r'login', views.UserLoginView, basename='user-login')
router.register(r'create', views.UserCreationView, basename='user-register')
router.register(r'profile-update', views.ProfileUpdateView, basename='profile-update')

urlpatterns = [
    url(r'^', include(router.urls)),
    ]