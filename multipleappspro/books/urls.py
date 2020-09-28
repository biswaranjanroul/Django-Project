from django.conf.urls import url
from .import views
urlpatterns=[
    url(r'^python/',views.python),
    url(r'^django/',views.django),
    url(r'^ui/',views.ui),
    url(r'^$',views.python)
]