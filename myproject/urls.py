from django.conf.urls import url
from myapp.views import hello

urlpatterns = [
    url(r'^$', hello, name='hello'),
]
