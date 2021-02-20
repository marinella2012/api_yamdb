from django.urls import path, include
from rest_framework.routers import DefaultRouter


from users.views import send_code, send_token, UserViewSet, MeViewSet


router = DefaultRouter()
router.register('users/me', MeViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('v1/auth/email/', send_code),
    path('v1/auth/token/', send_token),
    path('v1/', include(router.urls)),
]
