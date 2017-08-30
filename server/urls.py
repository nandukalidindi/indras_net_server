from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_agent/', views.get_agent, name='get_agent'),
    url(r'^get_matches/', views.get_matches, name='get_matches'),
    # url(r'^$', views.index, name='index'),
    # url(r'^$', views.index, name='index'),
]
