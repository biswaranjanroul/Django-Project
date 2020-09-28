"""testseriespro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from testseriesapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',views.login_view),
    url(r'^signup/',views.signup_view),
    url(r'^$',views.signup_view),
    url(r'^logout/', views.logout_view),
    url(r'^testdecs/',views.test_desc),
    url(r'^testserieshome/',views.test_home),
    url(r'^testserieshome2/',views.test_home2),
    url(r'^testserieshome3/',views.test_home3)

]