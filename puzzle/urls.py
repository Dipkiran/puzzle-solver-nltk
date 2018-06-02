from django.conf.urls import url
from . import views

app_name = 'puzzle'

urlpatterns = [
    url(r'^', views.page, name= 'index'),
    url(r'^puzzle/', views.page, name= 'index'),
]
