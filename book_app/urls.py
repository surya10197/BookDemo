from django.conf.urls import url
from .views import BookView

urlpatterns = [
    url(
        r'^$',
        BookView.as_view({
            'post': 'create',
            'get': 'list',
        }),
        name='books',
    ),

    url(
        r'^(?P<pk>[\w+]+)/$',
        BookView.as_view({
            'delete': 'destroy',
            'get': 'retrive',
        }),
        name='book-detail',
    ),
]
