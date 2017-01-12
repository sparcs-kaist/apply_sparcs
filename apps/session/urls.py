from django.conf.urls import url
from apps.session import views

urlpatterns = [
    url(r'^login', views.login),
    url(r'^callback',views.callback),
    url(r'^logout',views.logout),
    url(r'^unregister',views.unregister),
]
