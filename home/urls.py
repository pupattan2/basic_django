from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.dashboard, name='home'),
    url(r'dashboard', views.dashboard, name='dashboard'),
]