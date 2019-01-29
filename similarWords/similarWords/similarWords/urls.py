"""
Definition of urls for similarWords.
"""

from django.conf.urls import include, url
import searchHelper.views

urlpatterns = [
    url(r'^$', searchHelper.views.index, name='index'),
]
