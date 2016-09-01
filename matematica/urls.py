from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^home$', home , name='home'),
    url(r'^funcao1$', funcao1 , name='funcao1'),
]
