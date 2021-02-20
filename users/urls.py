from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import SendCode, SendToken


router = DefaultRouter()
#router.register('', , basename='')


urlpatterns = [
    path('email/', SendCode),
    path('token/', SendToken),
    path('', include(router.urls)),
]