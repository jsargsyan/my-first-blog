from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ask_post, name='ask_post'),
]