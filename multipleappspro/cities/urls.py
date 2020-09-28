from django.conf.urls import url
from .import views
urlpatterns=[
    url(r'^hyd/',views.hyd),
    url(r'^bang/',views.bang),
    url(r'^chennai/',views.chennai)
]