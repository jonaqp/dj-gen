from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^reservation/',
        include([
            url(r'^$', views.ReservationList.as_view(), name='list'),
            url(r'^create/$', views.ReservationCreate.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', views.ReservationUpdate.as_view(), name='update'),
            url(r'^(?P<pk>\d+)/delete/$', views.ReservationDelete.as_view(), name='delete'),
        ], namespace="reservation")),

    url(r'^mesa/',
            include([
                url(r'^$', views.ReservationMesaList.as_view(), name='list'),
            ], namespace="mesa")),

]
