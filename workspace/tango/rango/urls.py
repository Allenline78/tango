from django.conf.urls import patterns, url
from rango import views
urlpatterns = patterns('',
url(r'^$', views.rango, name='rango'),
url(r'^about/$', views.about, name='about'),
url(r'^populate/$', views.populate, name='populate'),
url(r'^category/(?P<categoryNameSlug>[\w\-]+)/$', views.category, name='category'),
url(r'^addCategory/$', views.addCategory, name='addCategory'),
url(r'^(?P<categoryNameSlug>[\w\-]+)/addPage/$', views.addPage, name='addPage'),
)
