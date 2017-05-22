from django.conf.urls import url
from . import views

# All Blog Url Define Here

urlpatterns = [

    url(r'^$', views.post_list, name='post_list'),

]