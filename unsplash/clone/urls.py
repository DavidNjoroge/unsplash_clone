from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
url('^$',views.index,name='index'),
url(r'^post/(\d+)',views.post,name='post'),
url(r'^tag/(\d+)',views.tag, name='tag'),
url(r'^search/',views.search,name='search_results')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
