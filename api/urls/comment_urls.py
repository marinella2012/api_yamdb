from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ..views import CommentViewSet

router = DefaultRouter()
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    'comment'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
