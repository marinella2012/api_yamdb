from django.urls import path, include
from rest_framework.routers import DefaultRouter


from users.views import SendCode, SendToken


router = DefaultRouter()
#router.register('', , basename='')


urlpatterns = [
    path('v1/auth/email/', SendCode),
    path('v1/auth/token/', SendToken),
    path('v1/users/', include(router.urls)),
]