from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'/register', RegisterViews.as_view() , basename='register')
router.register(r'/token_refresh',tokenViews.as_view() , basename='token_refresh')
router.register(r'/login', loginViews.as_view() , basename='login')
router.register(r'/Profile', ProfileViews.as_view() , basename='Profile')