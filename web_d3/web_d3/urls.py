"""mysite URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from blog.views import blog_index, blog_bs_test, blog_head_test
from d3.views import d3_index, d3_pop

#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', blog_index),
	url(r'^blog/bs_test$', blog_bs_test),
	url(r'^blog/head_test$', blog_head_test),
	url(r'^d3/$', d3_index),
	url(r'^d3/pop$', d3_pop),
]