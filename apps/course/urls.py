from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^process$', views.process)
]
