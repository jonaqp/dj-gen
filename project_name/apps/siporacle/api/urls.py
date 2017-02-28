# coding=utf-8
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'',
        include([
            url(r'^usuario/$', views.SolicitanteAPIListView.as_view()),
            url(r'^usuario/(?P<pk>[0-9]+)/$', views.SolicitanteAPIView.as_view()),
        ], namespace='api-usuario')),

]
