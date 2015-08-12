from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^decks/$', views.decks, name = 'decks'),
    url(r'^decks/review/(\d+)/$', views.decks_review, name = 'decks_review'),
    url(r'^classes/$', views.classes, name = 'classes'),
    url(r'^classes/new/$', views.classes_new, name = 'classes_new'),
    url(r'^classes/new/create/$', views.classes_new_create, name = 'classes_new_create'),
]