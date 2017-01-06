from django.conf.urls import url

from .views import IndexView

urlpatterns = [
    url(r'^user/$', IndexView.as_view(), name="index"),
]
