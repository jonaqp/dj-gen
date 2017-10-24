from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^restaurant/',
        include([
            url(r'^$', views.RestaurantList.as_view(), name='list'),
            url(r'^create/$', views.RestaurantCreate.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.RestaurantUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.RestaurantDelete.as_view(), name='delete'),
        ], namespace="restaurant")),
    url(r'^mesa/',
        include([
            url(r'^$', views.MesaList.as_view(), name='list'),
            url(r'^create/$', views.MesaCreate.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.MesaUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.MesaDelete.as_view(), name='delete'),
        ], namespace="mesa")),
    url(r'^menu/',
        include([
            url(r'^$', views.MenuList.as_view(), name='list'),
            url(r'^create/$', views.MenuCreate.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.MenuUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.MenuDelete.as_view(), name='delete'),
        ], namespace="menu")),
]
