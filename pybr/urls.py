from django.urls import path
from pybr.views import index, members

urlpatterns = [
    path('', index, name='index'),
    path('members/', members, name='members'),
]