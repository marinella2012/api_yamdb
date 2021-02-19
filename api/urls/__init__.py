from .category_urls import urlpatterns as category_urlpatterns
from .comment_urls import urlpatterns as comment_urlpatterns
from .genre_urls import urlpatterns as genre_urls_urlpatterns
from .review_urls import urlpatterns as review_urlpatterns
from .title_urls import urlpatterns as title_urls_urlpatterns

urlpatterns = []
urlpatterns += review_urlpatterns
urlpatterns += comment_urlpatterns
urlpatterns += category_urlpatterns
urlpatterns += title_urls_urlpatterns
urlpatterns += genre_urls_urlpatterns
