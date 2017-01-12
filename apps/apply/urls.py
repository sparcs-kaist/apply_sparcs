from django.conf.urls import url
from apps.apply import views
urlpatterns = [
    url(r'^$', views.submit_home),
    url(r'^submit', views.submit_data),
]