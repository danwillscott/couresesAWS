
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^delete$', views.delete),
    url(r'^edit/(?P<course_id>\w+)$', views.edit)
]
