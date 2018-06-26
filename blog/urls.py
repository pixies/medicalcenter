from django.urls import path

from .views import index, post_detail

app_name = 'blog'

urlpatterns = [
    path('', index),
    path('<int:pk>/', post_detail, name='detail'),
#    path('^(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
]
