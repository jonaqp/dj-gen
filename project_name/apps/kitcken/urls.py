from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^pedido/',
        include([
            url(r'^$', views.PedidoList.as_view(), name='list'),
            url(r'^(?P<pk>\d+)/update/$', views.PedidoUpdate.as_view(), name='update'),
        ], namespace="pedido")),


]
