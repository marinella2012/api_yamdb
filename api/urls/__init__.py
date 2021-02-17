from .review_urls import urlpatterns as review_urlpatterns
from .comment_urls import urlpatterns as comment_urlpatterns


urlpatterns = []
urlpatterns += review_urlpatterns
urlpatterns += comment_urlpatterns