from django.conf.urls import url

from . import views  # 자기자신이 속한 페키지 표현

# from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
