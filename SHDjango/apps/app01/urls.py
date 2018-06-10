from django.conf.urls import url
from app01.views import hello_world
from app01.index_handler import indexHandLer
from app01.search_handler import SearchHandler
from app01.detail_handler import DetailHandler

urlpatterns = [
    url(r'^hello/$', hello_world),
    url(r'^index/$', indexHandLer),
    url(r'^search/$', SearchHandler),
    url(r'^detail/$', DetailHandler)















]